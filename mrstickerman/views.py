from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import Product, Order
from .forms import CheckoutForm
from . import db
from datetime import datetime

# Create Blueprint for main views
views = Blueprint('views', __name__)

@views.route('/')
def index():
    """Display all products with search functionality"""
    # Get search query from request args
    search_query = request.args.get('search', '')
    
    if search_query:
        # Search products by name or description
        products = Product.query.filter(
            (Product.name.contains(search_query)) | 
            (Product.description.contains(search_query))
        ).all()
    else:
        # Get all products
        products = Product.query.all()
    
    return render_template('index.html', products=products, search_query=search_query)

@views.route('/product/<int:id>')
def product_detail(id):
    """Display product details"""
    product = Product.query.get_or_404(id)
    return render_template('product_detail.html', product=product)

@views.route('/order', methods=['GET', 'POST'])
def order():
    """Display basket and handle adding products"""
    # Get or create order in session
    if 'order_id' not in session:
        # Create a new order
        new_order = Order(status=False)
        db.session.add(new_order)
        db.session.commit()
        session['order_id'] = new_order.id
    
    # Handle POST request to add product to basket
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        if product_id:
            product = Product.query.get(product_id)
            if product:
                order = Order.query.get(session['order_id'])
                # Add product to order
                order.products.append(product)
                db.session.commit()
                flash(f'{product.name} added to basket!', 'success')
                return redirect(url_for('views.order'))
    
    # Get current order
    order = Order.query.get(session.get('order_id'))
    
    # Calculate total cost
    total_cost = 0
    if order and order.products:
        total_cost = sum(product.price for product in order.products)
    
    return render_template('basket.html', order=order, total_cost=total_cost)

@views.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    """Remove item from basket"""
    product_id = request.form.get('product_id')
    
    if 'order_id' in session:
        order = Order.query.get(session['order_id'])
        if order:
            product = Product.query.get(product_id)
            if product and product in order.products:
                # Remove only one instance of the product
                order.products.remove(product)
                db.session.commit()
                flash(f'{product.name} removed from basket.', 'info')
    
    return redirect(url_for('views.order'))

@views.route('/deleteorder', methods=['POST'])
def deleteorder():
    """Clear entire basket"""
    if 'order_id' in session:
        order = Order.query.get(session['order_id'])
        if order:
            # Clear all products from order
            order.products.clear()
            db.session.commit()
            flash('Basket cleared.', 'info')
    
    return redirect(url_for('views.order'))

@views.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """Display checkout form and process order completion"""
    # Check if there's an order
    if 'order_id' not in session:
        flash('Your basket is empty!', 'warning')
        return redirect(url_for('views.index'))
    
    order = Order.query.get(session['order_id'])
    
    # Check if order has products
    if not order or not order.products:
        flash('Your basket is empty!', 'warning')
        return redirect(url_for('views.index'))
    
    # Create checkout form
    form = CheckoutForm()
    
    if form.validate_on_submit():
        # Update order with customer details
        order.firstname = form.firstname.data
        order.surname = form.surname.data
        order.email = form.email.data
        order.phone = form.phone.data
        order.totalcost = sum(product.price for product in order.products)
        order.date = datetime.now()
        order.status = True  # Mark as completed
        
        db.session.commit()
        
        # Clear session
        session.pop('order_id', None)
        
        flash(f'Thank you for your order, {order.firstname}! Order confirmation sent to {order.email}.', 'success')
        return redirect(url_for('views.index'))
    
    # Calculate total for display
    total_cost = sum(product.price for product in order.products)
    
    return render_template('checkout.html', form=form, order=order, total_cost=total_cost)