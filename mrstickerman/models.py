from . import db
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

# Association table for many-to-many relationship between Order and Product
orderdetails = db.Table('orderdetails',
    sa.Column('order_id', sa.Integer, sa.ForeignKey('orders.id'), nullable=False),
    sa.Column('product_id', sa.Integer, sa.ForeignKey('products.id'), nullable=False)
)

class Product(db.Model):
    __tablename__ = 'products'
    
    # Primary key
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    
    # Product information
    name: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    description: Mapped[str] = mapped_column(sa.String(500), nullable=False)
    price: Mapped[float] = mapped_column(sa.Float, nullable=False)
    category: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    sticker_count: Mapped[int] = mapped_column(sa.Integer, nullable=False)
    size: Mapped[str] = mapped_column(sa.String(20), nullable=False)  # Size in cm (e.g., "3-6 cm")
    material: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    finish: Mapped[str] = mapped_column(sa.String(20), nullable=False)  # Glossy or Matte
    image_url: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    in_stock: Mapped[bool] = mapped_column(sa.Boolean, default=True, nullable=False)
    
    def __repr__(self):
        return f"<Product {self.name}>"

class Order(db.Model):
    __tablename__ = 'orders'
    
    # Primary key
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    
    # Order status (False = in basket, True = completed)
    status: Mapped[bool] = mapped_column(sa.Boolean, default=False, nullable=False)
    
    # Customer information (empty until checkout)
    firstname: Mapped[str] = mapped_column(sa.String(50), nullable=True)
    surname: Mapped[str] = mapped_column(sa.String(50), nullable=True)
    email: Mapped[str] = mapped_column(sa.String(100), nullable=True)
    phone: Mapped[str] = mapped_column(sa.String(20), nullable=True)
    
    # Order details
    totalcost: Mapped[float] = mapped_column(sa.Float, nullable=True)
    date: Mapped[sa.DateTime] = mapped_column(sa.DateTime, nullable=True)
    
    # Many-to-many relationship with Product through orderdetails table
    products = db.relationship('Product', secondary=orderdetails, backref='orders')
    
    def __repr__(self):
        return f"<Order {self.id}>"