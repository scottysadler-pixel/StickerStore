from flask import Blueprint, redirect, url_for, flash
from .models import Product
from . import db

# Create Blueprint for admin routes
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/dbseed')
def dbseed():
    """Populate database with sticker pack products"""
    
    # Clear existing products
    Product.query.delete()
    db.session.commit()
    
    # Create sticker pack products with Australian spelling and metric measurements
    products = [
        Product(
            name='Simpsons Pack',
            description='Bring Springfield to life with this amazing Simpsons sticker pack! Featuring unique designs of Homer, Marge, Bart, Lisa, Maggie, and all your favourite characters. Perfect for laptops, water bottles, notebooks, and more!',
            price=3.99,
            category='TV Shows & Movies',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='simpsons.webp',
            in_stock=True
        ),
        Product(
            name='Pokemon Pack',
            description='Catch them all with this fantastic Pokemon sticker collection! Includes all your favourite Pokemon from multiple generations. Colourful, vibrant designs that bring the world of Pokemon to your belongings!',
            price=4.99,
            category='Gaming & Online',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='pokemon.webp',
            in_stock=True
        ),
        Product(
            name='Anime Pack',
            description='Celebrate your love for anime with this diverse collection! Features characters from popular series, organised in a beautiful mix of art styles. Perfect for anime enthusiasts and collectors!',
            price=5.99,
            category='Pop Culture & Characters',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='anime.webp',
            in_stock=True
        ),
        Product(
            name='Star Wars Pack',
            description='May the Force be with you! This Star Wars sticker pack includes iconic characters, spaceships, and symbols from across the galaxy. Perfect for fans of the legendary space saga!',
            price=5.49,
            category='TV Shows & Movies',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='starwars.webp',
            in_stock=True
        ),
        Product(
            name='Minions Pack',
            description='Banana! These adorable Minions stickers will bring joy and laughter to your day. Featuring various Minion expressions and poses, perfect for kids and adults who love these lovable yellow characters!',
            price=5.99,
            category='Pop Culture & Characters',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='minions.webp',
            in_stock=True
        ),
        Product(
            name='Flowers Pack',
            description='Brighten up your belongings with this beautiful floral collection! Features a variety of colourful flower designs, perfect for adding a touch of nature and elegance to laptops, phones, and journals.',
            price=4.99,
            category='Animals & Nature',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Matte',
            image_url='flowers.webp',
            in_stock=True
        ),
        Product(
            name='Zelda Pack',
            description='Adventure awaits with this Legend of Zelda sticker pack! Includes Link, Zelda, and iconic symbols from Hyrule. Perfect for gamers and fans of this legendary series!',
            price=5.99,
            category='Gaming & Online',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='Zelda.webp',
            in_stock=True
        ),
        Product(
            name='Aliens Pack',
            description='Take me to your leader! This fun alien-themed sticker pack features quirky extraterrestrial designs, UFOs, and space themes. Perfect for sci-fi enthusiasts and space lovers!',
            price=4.49,
            category='Fun & Inspirational',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='aliens.webp',
            in_stock=True
        ),
        Product(
            name='Among Us Pack',
            description='Who is the impostor? These Among Us stickers feature colourful crewmates and impostors in various poses. Perfect for fans of this popular game!',
            price=4.99,
            category='Gaming & Online',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='among-us.webp',
            in_stock=True
        ),
        Product(
            name='Animals Pack',
            description='Wild and wonderful! This animal sticker collection features a diverse range of cute and realistic animal designs. Perfect for nature lovers and animal enthusiasts of all ages!',
            price=4.99,
            category='Animals & Nature',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Matte',
            image_url='animals.webp',
            in_stock=True
        ),
        Product(
            name='Bluey Pack',
            description='For real life! Bluey and Bingo stickers featuring your favourite Australian Blue Heeler family. Perfect for kids and fans of this beloved Australian TV show!',
            price=4.99,
            category='TV Shows & Movies',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='bluey.webp',
            in_stock=True
        ),
        Product(
            name='Skateboard Pack',
            description='Shred the gnar with this awesome skateboard-themed sticker collection! Features brands, tricks, and skate culture designs. Perfect for skaters and action sports enthusiasts!',
            price=5.49,
            category='Sports & Activities',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='Skate.webp',
            in_stock=True
        ),
        Product(
            name='Nike Pack',
            description='Just Do It! This Nike-inspired sticker pack features swooshes and athletic designs. Perfect for sports lovers and fitness enthusiasts!',
            price=5.99,
            category='Brands & Logos',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='Nike.webp',
            in_stock=True
        ),
        Product(
            name='Soccer Pack',
            description='Goal! This football sticker collection features team logos, balls, and soccer-themed designs. Perfect for fans of the beautiful game!',
            price=4.99,
            category='Sports & Activities',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='Soccer.webp',
            in_stock=True
        ),
        Product(
            name='Back to the Future Pack',
            description='Great Scott! Travel through time with these iconic Back to the Future stickers. Features the DeLorean, Doc, Marty, and memorable quotes from the trilogy!',
            price=5.99,
            category='TV Shows & Movies',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='BackToTheFuture.webp',
            in_stock=True
        ),
        Product(
            name='Frogs Pack',
            description='Ribbit! This adorable frog sticker collection features various frog species and cute amphibian designs. Perfect for nature lovers and frog enthusiasts!',
            price=4.49,
            category='Animals & Nature',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Matte',
            image_url='Frogs.webp',
            in_stock=True
        ),
        Product(
            name='JDM Pack',
            description='Japanese Domestic Market pride! Features iconic JDM car brands and tuning culture stickers. Perfect for car enthusiasts and JDM fans!',
            price=5.99,
            category='Transportation & Vehicles',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='JDM.webp',
            in_stock=True
        ),
        Product(
            name='Rainbow Pack',
            description='Brighten your day with this colourful rainbow sticker collection! Features vibrant colours and positive vibes. Perfect for spreading joy and colour everywhere!',
            price=4.49,
            category='Fun & Inspirational',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='Rainbow.webp',
            in_stock=True
        ),
        Product(
            name='Rock Music Pack',
            description='Rock on! This music-themed sticker pack celebrates rock legends, guitars, and music culture. Perfect for musicians and rock music fans!',
            price=5.49,
            category='Fun & Inspirational',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Glossy',
            image_url='Rock.webp',
            in_stock=True
        ),
        Product(
            name='Life Variety Pack',
            description='A mixed bag of life! This variety pack includes motivational quotes, fun designs, and colourful patterns. Perfect for those who love diversity!',
            price=4.99,
            category='Variety & Mixed',
            sticker_count=50,
            size='3-6 cm',
            material='Premium waterproof vinyl',
            finish='Matte',
            image_url='Life.webp',
            in_stock=True
        ),
    ]
    
    # Add all products to database
    for product in products:
        db.session.add(product)
    
    db.session.commit()
    
    flash(f'Database seeded successfully with {len(products)} products!', 'success')
    return redirect(url_for('views.index'))
