from . import db

# OrderDetail model for tracking product quantities in orders
class OrderDetail(db.Model):
    __tablename__ = 'orderdetails'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign keys
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    
    # Quantity of this product in the order
    quantity = db.Column(db.Integer, default=1, nullable=False)
    
    # Subtotal for this line item (quantity * price)
    subtotal = db.Column(db.Float, nullable=False)
    
    # Relationships
    product = db.relationship('Product', backref='order_details')
    
    def __repr__(self):
        return f"<OrderDetail Order:{self.order_id} Product:{self.product_id} Qty:{self.quantity}>"

class Product(db.Model):
    __tablename__ = 'products'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Product information
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    sticker_count = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(20), nullable=False)  # Size in cm (e.g., "3-6 cm")
    material = db.Column(db.String(100), nullable=False)
    finish = db.Column(db.String(20), nullable=False)  # Glossy or Matte
    image_url = db.Column(db.String(200), nullable=False)
    in_stock = db.Column(db.Boolean, default=True, nullable=False)
    
    def __repr__(self):
        return f"<Product {self.name}>"

class Order(db.Model):
    __tablename__ = 'orders'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Order status (False = in basket, True = completed)
    status = db.Column(db.Boolean, default=False, nullable=False)
    
    # Customer information (empty until checkout)
    firstname = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    
    # Delivery address
    address = db.Column(db.String(200))
    suburb = db.Column(db.String(100))
    state = db.Column(db.String(20))
    postcode = db.Column(db.String(10))
    
    # Order details
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    
    # Relationship with OrderDetail
    details = db.relationship('OrderDetail', backref='order', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<Order {self.id}>"