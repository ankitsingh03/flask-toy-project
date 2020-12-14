from flaskproperty import app


if __name__ == "__main__":
    app.run(debug=False)


@app.cli.command()
def dummyuser():
    from flaskproperty import db, bcrypt
    from flaskproperty.models import User
    hashed_password = bcrypt.generate_password_hash('123')\
                            .decode('utf-8')
    seller1 = User(username='seller1',
                   email="seller1@demo.com", password=hashed_password)
    hashed_password = bcrypt.generate_password_hash('123')\
                            .decode('utf-8')
    seller2 = User(username='seller2',
                   email="seller2@demo.com", password=hashed_password)
    db.session.add(seller1)
    db.session.add(seller2)
    db.session.commit()


@app.cli.command()
def dummypost():
    from flaskproperty import db
    from flaskproperty.models import User, Post
    post1 = Post(location='Bangalore',
                 detail="Enjoy a blissful living experience in JP North.\
                 This residential project encompasses 1 BHK flats in Mira\
                 Road East, Mira Road And Beyond and brings you the best \
                 of both the worlds – excellent aesthetics and\
                 exemplary lifestyle.Its unique highlights include\
                 facilities like 24/7 Water Supply, Sewage Treatment Plant, \
                 Lawn Tennis Court, And you can now buy your exclusive 1 BHK\
                 flat in this project at a price of Rs. 44.56 Lac - Rs. 44.56\
                 Lac.It has a carpet area ranging from 369.0 sq. ft. - 369.0\
                 sq. ft. contact me: 9001210121",
                 user_id=User.query
                             .filter_by(email='seller1@demo.com')
                             .first().id)
    post2 = Post(location='Mumbai',
                 detail="Enjoy a blissful living experience in JP North.\
                 This residential project encompasses 1 BHK flats in Mira\
                 Road East, Mira Road And Beyond and brings you the best \
                 of both the worlds – excellent aesthetics and\
                 exemplary lifestyle.Its unique highlights include\
                 facilities like 24/7 Water Supply, Sewage Treatment Plant, \
                 Lawn Tennis Court, And you can now buy your exclusive 1 BHK\
                 flat in this project at a price of Rs. 44.56 Lac - Rs. 44.56\
                 Lac.It has a carpet area ranging from 369.0 sq. ft. - 369.0\
                 sq. ft. contact me: 9001210121",
                 user_id=User.query
                             .filter_by(email='seller2@demo.com')
                             .first().id)
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
