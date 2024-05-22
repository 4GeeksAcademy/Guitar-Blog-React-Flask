
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
            ]
            db.session.add_all(classicals)
            db.session.commit()
    
            print("Demo database successfully created.")
        except Exception as e:
            db.session.rollback()
            print(f"Error while running the script: {e}")
