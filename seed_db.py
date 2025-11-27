#!/usr/bin/env python3
"""
Database seeding script for Mr Stickerman
Populates the database with sample sticker products
"""
from mrstickerman import create_app, db
from mrstickerman.models import Product

app = create_app()

def seed_database():
    """Add sample products to the database."""
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Clear existing products
        Product.query.delete()
        
        # Sample products based on available images
        products = [
            Product(
                name="Simpsons Pack",
                description="Classic Simpsons characters - Homer, Marge, Bart, Lisa, and more! Perfect for fans of the iconic TV show.",
                price=3.99,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="simpsons.webp",
                in_stock=True
            ),
            Product(
                name="Pokemon Pack",
                description="Catch 'em all with this amazing Pokemon sticker collection! Features Pikachu and many popular Pokemon.",
                price=4.99,
                category="Gaming & Online",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="pokemon.webp",
                in_stock=True
            ),
            Product(
                name="Anime Pack",
                description="Popular anime characters and symbols. Perfect for anime enthusiasts and collectors.",
                price=5.99,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="anime.webp",
                in_stock=True
            ),
            Product(
                name="Star Wars Pack",
                description="May the Force be with you! Classic Star Wars characters and iconic symbols from a galaxy far, far away.",
                price=5.49,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="starwars.webp",
                in_stock=True
            ),
            Product(
                name="Minions Pack",
                description="Despicably adorable Minions stickers! Perfect for kids and fans of the Despicable Me franchise.",
                price=5.99,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="minions.webp",
                in_stock=True
            ),
            Product(
                name="Flowers Pack",
                description="Beautiful floral designs perfect for decorating laptops, water bottles, and journals.",
                price=4.99,
                category="Animals & Nature",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Matte",
                image_url="flowers.webp",
                in_stock=True
            ),
            Product(
                name="Among Us Pack",
                description="Sus! Popular Among Us characters in various colours. Perfect for gamers.",
                price=4.49,
                category="Gaming & Online",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="among-us.webp",
                in_stock=True
            ),
            Product(
                name="Animals Pack",
                description="Cute and colourful animal stickers featuring cats, dogs, pandas, and more.",
                price=4.99,
                category="Animals & Nature",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="animals.webp",
                in_stock=True
            ),
            Product(
                name="Superheroes Pack",
                description="Amazing superhero stickers featuring popular comic book characters and symbols.",
                price=5.99,
                category="Superheroes & Comics",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="superheroes.webp",
                in_stock=True
            ),
            Product(
                name="Back to the Future Pack",
                description="Great Scott! Classic Back to the Future themed stickers with the DeLorean and more.",
                price=5.49,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="BackToTheFuture.webp",
                in_stock=True
            ),
            Product(
                name="Skateboard Pack",
                description="Cool skateboarding-themed stickers perfect for skaters and action sports enthusiasts.",
                price=4.99,
                category="Sports & Activities",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="Skate.webp",
                in_stock=True
            ),
            Product(
                name="Brand Logos Pack",
                description="Popular brand logos and symbols. Show your brand loyalty!",
                price=4.99,
                category="Brands & Logos",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="Logos.webp",
                in_stock=True
            ),
            # TV Shows & Movies - 6 new products
            Product(
                name="Bluey Pack",
                description="Fun and colourful Bluey stickers featuring the beloved Australian cartoon family. Perfect for kids!",
                price=4.99,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="bluey.webp",
                in_stock=True
            ),
            Product(
                name="Disney Pack",
                description="Magical Disney character stickers featuring your favourite classic and modern Disney heroes.",
                price=5.99,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="disney2.webp",
                in_stock=True
            ),
            Product(
                name="Game of Thrones Pack",
                description="Winter is coming! Epic Game of Thrones stickers featuring houses, dragons, and iconic characters.",
                price=5.49,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Matte",
                image_url="gameofthrones.webp",
                in_stock=True
            ),
            Product(
                name="Paw Patrol Pack",
                description="No job is too big, no pup is too small! Adorable Paw Patrol stickers for young fans.",
                price=4.49,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="paw-patrol.webp",
                in_stock=True
            ),
            Product(
                name="Shrek Pack",
                description="Get out of my swamp! Hilarious Shrek stickers featuring the lovable ogre and friends.",
                price=4.99,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="shrek.webp",
                in_stock=True
            ),
            Product(
                name="SpongeBob Pack",
                description="Are you ready kids? SpongeBob SquarePants stickers from Bikini Bottom for fans of all ages.",
                price=4.49,
                category="TV Shows & Movies",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="spongebob.webp",
                in_stock=True
            ),
            # Gaming & Online - 2 new products
            Product(
                name="Roblox Pack",
                description="Awesome Roblox stickers featuring popular game characters and iconic symbols from the platform.",
                price=4.99,
                category="Gaming & Online",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="roblox.webp",
                in_stock=True
            ),
            Product(
                name="Space Aliens Pack",
                description="Out-of-this-world alien stickers featuring UFOs, extraterrestrials, and cosmic creatures.",
                price=4.49,
                category="Gaming & Online",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="aliens.webp",
                in_stock=True
            ),
            # Pop Culture & Characters - 7 new products
            Product(
                name="Anime Collection Pack",
                description="Extended anime collection with even more popular characters and symbols for anime lovers.",
                price=5.49,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="anime5.webp",
                in_stock=True
            ),
            Product(
                name="Paris Pack",
                description="Romantic Paris-themed stickers featuring the Eiffel Tower, French culture, and Parisian vibes.",
                price=4.99,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Matte",
                image_url="paris.webp",
                in_stock=True
            ),
            Product(
                name="One Direction Pack",
                description="Directioners unite! One Direction stickers featuring the iconic boy band members.",
                price=4.99,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="one-direction.webp",
                in_stock=True
            ),
            Product(
                name="Rock Music Pack",
                description="Rock on! Awesome rock music stickers featuring guitars, skulls, and rock band vibes.",
                price=4.99,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="Rock.webp",
                in_stock=True
            ),
            Product(
                name="Skulls Pack",
                description="Edgy skull stickers with various artistic designs. Perfect for those who love dark aesthetics.",
                price=4.49,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Matte",
                image_url="skulls.webp",
                in_stock=True
            ),
            Product(
                name="Captions Pack",
                description="Fun caption and quote stickers with witty sayings and expressions for any occasion.",
                price=3.99,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="captions.webp",
                in_stock=True
            ),
            Product(
                name="Captions 2 Pack",
                description="More hilarious captions and quotes! Express yourself with these fun text stickers.",
                price=3.99,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="captions2.webp",
                in_stock=True
            ),
            Product(
                name="Captions 3 Pack",
                description="Even more captions! The ultimate collection of funny and inspiring quote stickers.",
                price=3.99,
                category="Pop Culture & Characters",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="captions3.webp",
                in_stock=True
            ),
            # Animals & Nature - 5 new products
            Product(
                name="Animals 2 Pack",
                description="More adorable animal stickers! Additional cute creatures to add to your collection.",
                price=4.99,
                category="Animals & Nature",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="animals2.webp",
                in_stock=True
            ),
            Product(
                name="Frogs Pack",
                description="Hoppy frog stickers featuring cute and colourful frogs in various poses and styles.",
                price=4.49,
                category="Animals & Nature",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="Frogs.webp",
                in_stock=True
            ),
            Product(
                name="Cactus Pack",
                description="Prickly but cute! Desert cactus stickers with succulents and southwestern vibes.",
                price=4.49,
                category="Animals & Nature",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Matte",
                image_url="cactus2.webp",
                in_stock=True
            ),
            Product(
                name="Cartoon Pigs Pack",
                description="Oink oink! Adorable cartoon pig stickers featuring cute piggies in various poses.",
                price=4.49,
                category="Animals & Nature",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="cartoon-pigs.webp",
                in_stock=True
            ),
            Product(
                name="Breast Cancer Awareness Pack",
                description="Pink ribbon breast cancer awareness stickers. Show your support for the cause.",
                price=4.99,
                category="Animals & Nature",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="breast-cancer.webp",
                in_stock=True
            ),
            # Superheroes & Comics - 2 new products
            Product(
                name="Deadpool Pack",
                description="Maximum effort! Hilarious Deadpool stickers featuring the merc with a mouth.",
                price=5.49,
                category="Superheroes & Comics",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="deadpool.webp",
                in_stock=True
            ),
            Product(
                name="Iron Man Pack",
                description="I am Iron Man! Epic Iron Man stickers featuring Tony Stark and his iconic suits.",
                price=5.49,
                category="Superheroes & Comics",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="ironman.webp",
                in_stock=True
            ),
            # Sports & Activities - 1 new product
            Product(
                name="Craft Beer Pack",
                description="Cheers! Craft beer stickers featuring breweries, hops, and beer-themed designs.",
                price=4.49,
                category="Sports & Activities",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="beer.webp",
                in_stock=True
            ),
            # Brands & Logos - 3 new products
            Product(
                name="Nike Pack",
                description="Just Do It! Nike stickers featuring the iconic swoosh and athletic designs.",
                price=4.99,
                category="Brands & Logos",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="Nike.webp",
                in_stock=True
            ),
            Product(
                name="JDM Pack",
                description="Japanese Domestic Market stickers for car enthusiasts. Racing and automotive designs.",
                price=4.99,
                category="Brands & Logos",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="JDM.webp",
                in_stock=True
            ),
            Product(
                name="Logos 2 Pack",
                description="Even more popular brand logos and symbols. Expand your brand collection!",
                price=4.99,
                category="Brands & Logos",
                sticker_count=50,
                size="3-6 cm",
                material="Premium waterproof vinyl",
                finish="Glossy",
                image_url="logos2.webp",
                in_stock=True
            ),
        ]
        
        # Add all products to the database
        for product in products:
            db.session.add(product)
        
        db.session.commit()
        print(f"Successfully added {len(products)} products to the database!")

if __name__ == '__main__':
    seed_database()
