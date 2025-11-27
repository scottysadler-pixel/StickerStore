from flask import Blueprint, render_template, request, redirect, url_for, session
from datetime import datetime
from . import db
from .models import Product, Order, OrderDetail
from .forms import CheckoutForm
import random

# Create views blueprint
views = Blueprint('views', __name__)

def get_or_create_order():
    """Get the current basket order or create a new one."""
    order_id = session.get('order_id')
    
    if order_id:
        order = Order.query.get(order_id)
        # Check if order exists and is still in basket status
        if order and not order.status:
            return order
    
    # Create new order for basket
    order = Order(status=False)
    db.session.add(order)
    db.session.commit()
    session['order_id'] = order.id
    return order

@views.route('/')
def index():
    """Landing page with sectioned layout or full catalog when searching."""
    search_query = request.args.get('search', '').strip()
    
    if search_query:
        # Show full catalog filtered by search
        products = Product.query.filter(
            (Product.name.contains(search_query)) | 
            (Product.description.contains(search_query)) |
            (Product.category.contains(search_query))
        ).all()
        return render_template('index.html', products=products, search_query=search_query)
    
    # Sectioned layout
    # New Arrivals: 6 most recently added products
    new_arrivals = Product.query.order_by(Product.id.desc()).limit(6).all()
    
    # Featured Products: 6 random products
    all_products = Product.query.all()
    featured_products = random.sample(all_products, min(6, len(all_products))) if all_products else []
    
    # Browse Categories: Get unique categories
    categories = db.session.query(Product.category).distinct().all()
    categories = [cat[0] for cat in categories]
    
    return render_template('index.html', 
                         new_arrivals=new_arrivals,
                         featured_products=featured_products,
                         categories=categories,
                         search_query=None)

@views.route('/product/<int:product_id>')
def product_details(product_id):
    """Display product details page."""
    product = Product.query.get_or_404(product_id)
    return render_template('product_details.html', product=product)

@views.route('/basket')
def basket():
    """Display basket with items, quantities, and totals."""
    order = get_or_create_order()
    
    # Calculate total
    total = sum(detail.subtotal for detail in order.details)
    
    return render_template('basket.html', order=order, total=total)

@views.route('/order', methods=['POST'])
def add_to_order():
    """Add a product to the basket or increment quantity if already exists."""
    product_id = request.form.get('product_id', type=int)
    
    if not product_id:
        return redirect(url_for('views.index'))
    
    product = Product.query.get_or_404(product_id)
    order = get_or_create_order()
    
    # Check if product already exists in this order
    existing_detail = OrderDetail.query.filter_by(
        order_id=order.id,
        product_id=product_id
    ).first()
    
    if existing_detail:
        # Increment quantity
        existing_detail.quantity += 1
        existing_detail.subtotal = existing_detail.quantity * product.price
    else:
        # Create new order detail
        detail = OrderDetail(
            order_id=order.id,
            product_id=product_id,
            quantity=1,
            subtotal=product.price
        )
        db.session.add(detail)
    
    db.session.commit()
    return redirect(url_for('views.basket'))

@views.route('/updatequantity', methods=['POST'])
def update_quantity():
    """Update the quantity of a product in the basket."""
    product_id = request.form.get('product_id', type=int)
    new_quantity = request.form.get('quantity', type=int)
    
    if not product_id or new_quantity is None:
        return redirect(url_for('views.basket'))
    
    order = get_or_create_order()
    
    # Find the order detail
    detail = OrderDetail.query.filter_by(
        order_id=order.id,
        product_id=product_id
    ).first()
    
    if detail:
        if new_quantity <= 0:
            # Remove item if quantity is 0 or negative
            db.session.delete(detail)
        else:
            # Update quantity and subtotal
            detail.quantity = new_quantity
            detail.subtotal = detail.quantity * detail.product.price
        
        db.session.commit()
    
    return redirect(url_for('views.basket'))

@views.route('/removeitem', methods=['POST'])
def remove_item():
    """Remove an item from the basket."""
    product_id = request.form.get('product_id', type=int)
    
    if not product_id:
        return redirect(url_for('views.basket'))
    
    order = get_or_create_order()
    
    # Find and delete the order detail
    detail = OrderDetail.query.filter_by(
        order_id=order.id,
        product_id=product_id
    ).first()
    
    if detail:
        db.session.delete(detail)
        db.session.commit()
    
    return redirect(url_for('views.basket'))

@views.route('/category/<category_name>')
def category(category_name):
    """Display products filtered by category."""
    products = Product.query.filter_by(category=category_name).all()
    
    return render_template('category.html', 
                          products=products, 
                          category_name=category_name)


@views.route('/shop')
def shop():
    """Display all products."""
    products = Product.query.filter_by(in_stock=True).all()
    
    return render_template('shop.html', products=products)


@views.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """Handle checkout process."""
    order = get_or_create_order()
    form = CheckoutForm()
    
    if form.validate_on_submit():
        # Update order with customer details
        order.firstname = form.firstname.data
        order.surname = form.surname.data
        order.email = form.email.data
        order.phone = form.phone.data
        order.address = form.address.data
        order.suburb = form.suburb.data
        order.state = form.state.data
        order.postcode = form.postcode.data
        order.status = True  # Mark as completed
        order.date = datetime.now()
        
        # Calculate and save total cost
        order.totalcost = sum(detail.subtotal for detail in order.details)
        
        db.session.commit()
        
        # Clear session
        session.pop('order_id', None)
        
        return render_template('order_confirmation.html', order=order)
    
    # Calculate total for display
    total = sum(detail.subtotal for detail in order.details)
    
    return render_template('checkout.html', form=form, order=order, total=total)