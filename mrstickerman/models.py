from . import db

# Association table for many-to-many relationship between Order and Product
orderdetails = db.Table('orderdetails',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), nullable=False),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), nullable=False)
)

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
    
    # Order details
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    
    # Many-to-many relationship with Product through orderdetails table
    products = db.relationship('Product', secondary=orderdetails, backref='orders')
    
    def __repr__(self):
        return f"<Order {self.id}>"