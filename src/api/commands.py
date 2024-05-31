
import click
from api.models import db, User, Electric, Acoustic, Classical, Favorites

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    @app.cli.command("insert-test-users") # name of our command
    @click.argument("count") # argument of out command
    def insert_test_users(count):
        print("Creating test users")
        for x in range(1, int(count) + 1):
            user = User()
            user.email = "test_user" + str(x) + "@test.com"
            user.password = "123456"
            user.is_active = True
            db.session.add(user)
            db.session.commit()
            print("User: ", user.email, " created.")

        print("All test users created")

    @app.cli.command("insert-test-data")
    def insert_test_data():
        db.drop_all()
        db.create_all()
        try: 
            users = [
                User(email="victoria@gmail.com",
                     password="Victoria32++",
                     first_name="Victoria",
                     last_name="Smith",
                     is_active=True),
                User(email="rose@gmail.com",
                     password="Rose32++",
                     first_name="Rose",
                     last_name="Johnson",
                     is_active=True),
                User(email="osianjorge@gmail.com",
                     password="Osian42++",
                     first_name="Osian",
                     last_name="Jorge",
                     is_active=True),
                User(email="frankluis1923@gmail.com",
                     password="Frank32++",
                     first_name="Frank",
                     last_name="Luis",
                     is_active=True),
                User(email="b.muruacarreras@gmail.com",
                     password="Bruno22++",
                     first_name="Bruno",
                     last_name="Murua",
                     is_active=True),
                User(email="lucy_daldeau@outlook.com",
                     password="Lucia30++",
                     first_name="Lucy",
                     last_name="Daldeau",
                     is_active=True)
            ]
            db.session.add_all(users)
            db.session.commit()
    
            electrics = [
                Electric(model="Stratocaster",
                         scale=25,
                         price=1500,
                         color="Red",
                         manufacturer="Fender",
                         pickups="Single-coil",
                         image="https://images.unsplash.com/photo-1561758423-4a993d30afea?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8ZmVuZGVyJTIwc3RyYXRvY2FzdGVyfGVufDB8fDB8fHww",
                         description="The Fender Stratocaster is an iconic electric guitar known for its bright, cutting tone and versatile single-coil pickups. Its contoured body and smooth playability make it a favorite among guitarists of all genres."),
                Electric(model="Les Paul",
                         scale=24,
                         price=2000,
                         color="Black",
                         manufacturer="Gibson",
                         pickups="Humbucker",
                         image="https://images.unsplash.com/photo-1456948927036-ad533e53865c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGdpYnNvbiUyMHNnfGVufDB8fDB8fHww",
                         description="The Gibson Les Paul is a legendary electric guitar, renowned for its thick, rich sound and powerful humbucker pickups. Its solid body and distinctive shape contribute to its sustain and resonance."),
                Electric(model="SG",
                         scale=24,
                         price=1800,
                         color="Cherry",
                         manufacturer="Gibson",
                         pickups="Humbucker",
                         image="https://images.unsplash.com/photo-1591365437381-2db81d59f1e0?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGdpYnNvbnxlbnwwfHwwfHx8MA%3D%3D",
                         description="The Gibson SG is celebrated for its lightweight, double-cutaway body and aggressive tone. Its humbucker pickups deliver a powerful sound, making it a staple in rock music."),
                Electric(model="Telecaster",
                         scale=25,
                         price=1400,
                         color="Butterscotch",
                         manufacturer="Fender",
                         pickups="Single-coil",
                         image="https://images.unsplash.com/photo-1690432950649-a5cc3ca4b547?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGZlbmRlciUyMHRlbGVjYXN0ZXJ8ZW58MHx8MHx8fDA%3D",
                         description="The Fender Telecaster is known for its bright, cutting tone and straightforward design. Its single-coil pickups provide a twangy sound, perfect for country and rock genres."),
                Electric(model="Jazzmaster",
                         scale=25,
                         price=1600,
                         color="Sunburst",
                         manufacturer="Fender",
                         pickups="Single-coil",
                         image="https://images.unsplash.com/photo-1520166012956-add9ba0835cb?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGZlbmRlciUyMGphenptYXN0ZXJ8ZW58MHx8MHx8fDA%3D",
                         description="The Fender Jazzmaster offers a unique tonal palette with its offset body and distinctive single-coil pickups. It's favored by indie and alternative musicians for its versatility and smooth playability."),
                Electric(model="Pacifico",
                         scale=25,
                         price=1800,
                         color="Indigo Blue",
                         manufacturer="Yamaha",
                         pickups="Humbucker",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQp2UEYvXP63_szRbvfeNxxtKaVLAKAN8wCA&s",
                         description="The Yamaha Pacifica offers a unique tonal palette with its offset body and distinctive single-coil pickups. It's favored by indie and alternative musicians for its versatility and smooth playability."),
                Electric(model="Explorer",
                         scale=24,
                         price=1900,
                         color="White",
                         manufacturer="Gibson",
                         pickups="Humbucker",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS95azAUDIykDx_JD2XrCOb8-P6P3GOW94pBA&s",
                         description="The Gibson Explorer is known for its bold design and powerful sound. Its humbucker pickups and solid body make it a favorite for rock and metal genres."),
                Electric(model="Firebird",
                         scale=25,
                         price=2100,
                         color="Vintage Sunburst",
                         manufacturer="Gibson",
                         pickups="Mini-Humbucker",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUmt53UIduxcX2o0kN7NCG8XLcgYl0K-B5ww&s",
                         description="The Gibson Firebird features a unique reverse body design and mini-humbucker pickups, offering a bright, clear tone with excellent sustain."),
                Electric(model="Mustang",
                         scale=24,
                         price=1300,
                         color="Blue",
                         manufacturer="Fender",
                         pickups="Single-coil",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqXLOqiqPURm0NMd9tmAuS66yu4f3zvQP8Ag&s",
                         description="The Fender Mustang is a short-scale electric guitar, known for its distinctive tone and lightweight body. Its single-coil pickups and dynamic vibrato system make it popular among alternative and indie musicians."),
                Electric(model="Rickenbacker 330",
                         scale=24,
                         price=2200,
                         color="Jetglo",
                         manufacturer="Rickenbacker",
                         pickups="Single-coil",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiylv6tqnzlViiuXuehu_lJYW9zP_mTJi2SQ&s",
                         description="The Rickenbacker 330 is renowned for its jangly, bright tone and unique body shape. Its single-coil pickups and semi-hollow construction make it a staple in rock and pop music."),
            ]

            db.session.add_all(electrics)
            db.session.commit()

            acoustics = [
                Acoustic(model="D-28",
                         scale=25,
                         price=3000,
                         color="Natural",
                         manufacturer="Martin",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbQvZTlsszJC3XNJBIMGtWsiEWAE5VFLRXvw&s",
                         description="The Martin D-28 is a classic acoustic guitar known for its powerful, balanced tone and excellent projection. Its solid wood construction and dreadnought body make it a favorite among professionals."),
                Acoustic(model="J-45",
                         scale=24,
                         price=2500,
                         color="Sunburst",
                         manufacturer="Gibson",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAniubG_pYgv_dCERPlygL6djfyHYx7acr-g&s",
                         description="The Gibson J-45 is an iconic acoustic guitar, prized for its warm, full sound and exceptional playability. Its round-shoulder body and sunburst finish make it visually striking."),
                Acoustic(model="FG800",
                         scale=25,
                         price=500,
                         color="Black",
                         manufacturer="Yamaha",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGPO53vZT5jBr-b8XLFBOeYB1Fbtqb-9id-g&s",
                         description="The Yamaha FG800 is a highly regarded entry-level acoustic guitar, offering great tone and build quality at an affordable price. Its solid top and traditional body shape provide a balanced sound."),
                Acoustic(model="000-15M",
                         scale=25,
                         price=1300,
                         color="Mahogany",
                         manufacturer="Martin",
                         image="https://tobiasmusic.com/cdn/shop/files/martin-00015m-mahogany-guitar-3_2eb08b00-9758-474b-9cd2-1756971f39ee_600x.jpg?v=1690002035",
                         description="The Martin 000-15M features an all-mahogany body, offering a warm, rich tone with excellent midrange presence. Its smaller 000 body size makes it comfortable to play."),
                Acoustic(model="DR-100",
                         scale=25,
                         price=150,
                         color="Sunburst",
                         manufacturer="Epiphone",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxPZjDEuFwrEiWtfxHzoBVjb9xsbmefN9ueg&s",
                         description="The Epiphone DR-100 is a budget-friendly acoustic guitar, ideal for beginners. Its dreadnought body and sunburst finish provide a classic look and sound."),
                Acoustic(model="FGX5 NT",
                         scale=25,
                         price=1150,
                         color="Natural",
                         manufacturer="Yamaha",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9gWKeWwGS9xD5JKMzAKPwk4S4gmxPj9ZKfw&s",
                         description="The Yamaha FGX5 NT is a budget-friendly acoustic guitar, ideal for experts. Its dreadnought body and sunburst finish provide a classic look and sound."),
                Acoustic(model="D-18",
                         scale=25,
                         price=2900,
                         color="Natural",
                         manufacturer="Martin",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8ONZcCwPKqR9VAFcLqmnwgaS9c5d6HIyMZw&s",
                         description="The Martin D-18 is celebrated for its powerful, clear tone and solid mahogany back and sides. Its dreadnought body provides excellent projection and depth."),
                Acoustic(model="Songwriter",
                         scale=25,
                         price=3200,
                         color="Natural",
                         manufacturer="Gibson",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQte7Yb5a_1T1y9wfftnzpdyoV6qzNAUWpwHA&s",
                         description="The Gibson Songwriter is known for its bright, balanced tone and excellent playability. Its rosewood back and sides and dreadnought body shape make it a versatile choice for various styles."),
                Acoustic(model="L-00",
                         scale=24,
                         price=2600,
                         color="Vintage Sunburst",
                         manufacturer="Gibson",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3IRCN3P0WXtfnLXWCUGJqFkaCySThDX1kQA&s",
                         description="The Gibson L-00 offers a distinctively warm, balanced tone with its small body shape and solid construction. It's favored for blues and fingerstyle playing."),
                Acoustic(model="F7 Paco",
                         scale=25,
                         price=2300,
                         color="Natural",
                         manufacturer="Cordoba",
                         image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgxFiGvWJo7zOfJxIsUEA42DNnWNHPN-BWew&s",
                         description="The Cordoba F7 Paco is inspired by the legendary flamenco guitarist Paco de Lucía. Its solid cedar top and rosewood back and sides provide a warm, resonant tone perfect for flamenco and classical styles."),
            ]

            db.session.add_all(acoustics)
            db.session.commit()

            classicals = [
                Classical(model="C5",
                          scale=25,
                          price=400,
                          color="Natural",
                          manufacturer="Cordoba",
                          image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIPNZWySLcENbNmoeNx10QUQsknV-J_-f8Pg&s",
                          description="The Cordoba C5 is a well-crafted classical guitar, known for its rich, resonant tone and excellent playability. Its solid cedar top and mahogany back and sides provide a warm sound."),
                Classical(model="CG122MCH",
                          scale=25,
                          price=350,
                          color="Natural",
                          manufacturer="Yamaha",
                          image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGt8BwcV_PUFOqDNL6D__tohrvPQ0cUzKJLw&s",
                          description="The Yamaha CG122MCH is a quality classical guitar, offering a balanced tone and comfortable playability. Its solid cedar top and nato back and sides make it a great choice for students."),
                Classical(model="C40",
                          scale=25,
                          price=150,
                          color="Natural",
                          manufacturer="Yamaha",
                          image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNCWoGYfLDYWj4Qc4AFmMnbolZMLYOXPDRTw&s",
                          description="The Yamaha C40 is an affordable classical guitar, perfect for beginners. Its spruce top and meranti back and sides provide a clear, balanced tone."),
                Classical(model="GC1CE",
                          scale=25,
                          price=500,
                          color="Black",
                          manufacturer="Takamine",
                          image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRv6gMDrGDiH6QgHqGe8hXRcgE4VUoDc8XEg&s",
                          description="The Takamine GC1CE is an electric-acoustic classical guitar, offering a warm, rich tone with the added versatility of built-in electronics. Its black finish and cutaway body make it stylish and functional."),
                Classical(model="Protege C1M",
                          scale=25,
                          price=200,
                          color="Natural",
                          manufacturer="Cordoba",
                          image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx0ubGQZrm-zzRhiPpG-oAhDP0YXGZaY7_kw&s",
                          description="The Cordoba Protege C1M is a great entry-level classical guitar, offering excellent playability and a warm, full sound. Its spruce top and mahogany back and sides provide a balanced tone."),
                Classical(model="Yamaha C40II",
                          scale=25,
                          price=150,
                          color="Natural",
                          manufacturer="Yamaha",
                          image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQixYq9Tg-CV_uXZqwFDb4UeO_ZQ3wv7SiQkg&s",
                          description="The Yamaha C40II is a highly regarded entry-level classical guitar, known for its excellent build quality and rich, warm sound."),
                Classical(model="Alhambra 3C",
                          scale=25,
                          price=600,
                          color="Natural",
                          manufacturer="Alhambra",
                          image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZv8ev10Mupvlcjqr1Ocw7uOahXKZp8M4gUg&s",
                          description="The Alhambra 3C is a mid-range classical guitar, known for its bright, clear tone and high-quality craftsmanship. Its solid cedar top and mahogany back and sides offer excellent resonance."),
                Classical(model="Kremona Solea",
                          scale=25,
                          price=1500,
                          color="Natural",
                          manufacturer="Kremona",
                          image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEnJOPgVHX76cj6ngCbavOfLkaePY7iAQThQ&s",
                          description="The Kremona Solea is a professional-grade classical guitar, renowned for its warm, balanced tone and impeccable craftsmanship. Its solid cedar top and rosewood back and sides provide rich, complex sound."),
                Classical(model="La Patrie Etude",
                          scale=25,
                          price=500,
                          color="Natural",
                          manufacturer="La Patrie",
                          image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMJOWkaGFCnid2aJLKLp8B01wuRhQEetjGFA&s",
                          description="The La Patrie Etude is an excellent student guitar, offering great playability and a rich, full sound. Its solid cedar top and wild cherry back and sides provide a unique tonal character."),
                Classical(model="Jose Ramirez 2NE",
                          scale=25,
                          price=2000,
                          color="Natural",
                          manufacturer="Jose Ramirez",
                          image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ8xt117k2VV3V95LhUuWE_dyRGa7WuN9C5Q&s",
                          description="The Jose Ramirez 2NE is a top-tier classical guitar, known for its powerful, expressive tone and superb craftsmanship. Its solid cedar top and rosewood back and sides provide excellent projection and sustain."),
            ]

            db.session.add_all(classicals)
            db.session.commit()

    
            print("Demo database successfully created.")
        except Exception as e:
            db.session.rollback()
            print(f"Error while running the script: {e}")
