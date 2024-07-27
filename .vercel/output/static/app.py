from src import create_app

app = create_app()

def postFromID(id):
    from src.posts.routes import posts
    from src import models

    return models.Post.query.filter_by(id).first().title

if __name__ == '__main__':
    app.run(debug=True)


# >>> from run import app
# >>> app.app_context().push()
# >>> from src import db
# >>> from src.models import User, Post
# >>> User.Query.all()


# >>> from src import app, db
# >>> app.app_context().push()
# >>> db.create_all()
# >>> from src import User, Post
# >>> user_1 = User(username='Sam', email='S@demo.com', password='password')
# >>> db.session.add(user_1)
# >>> user_2 = User(username='John', email='J@demo.com', password='pez')
# >>> db.session.add(user-2)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: name 'user' is not defined. Did you mean: 'User'?
# >>> db.session.add(user_2)
# >>> db.session.commit()
# >>> User.query.all()
# [User('Sam', 'S@demo.com', 'default.jpg'), User('John', 'J@demo.com', 'default.jpg')]
# >>> User.query.filter_by(username='Sam').all()
# [User('Sam', 'S@demo.com', 'default.jpg')]
# >>> user = User.query.filter_by(username='John').first()
# >>> user
# User('John', 'J@demo.com', 'default.jpg')
# >>> user.id
# 2
# >>> post_1 = Post(title='Blog 1: Good Day', content='First post is soooo fun', user_id=u
# ser.id)
# >>> db.session.add(post_1)
# >>> db.session.add(post_2)
# >>> db.session.commit()
# >>> user.posts
# [User('Blog 1: Good Day', '2023-12-20 22:22:22.403855', User('Blog 2: social mdia', '2023-12-20 22:22:22.403855']
# >>> user.posts
# [User('Blog 1: Good Day', '2023-12-20 22:22:22.403855', User('Blog 2: social mdia', '2023-12-20 22:22:22.403855']
# >>> user.posts
# [User('Blog 1: Good Day', '2023-12-20 22:22:22.403855', User('Blog 2: social mdia', '2023-12-20 22:22:22.403855']
# >>> for post in user.posts: \
#         ... print(post.title)
# ...
# Blog 1: Good Day
# Blog 2: social mdia
#                >>>
# >>> hashed_pw = bcrypt.generate_password_hash('testing').decode('utf-8')
# >>> bcrypt.check_password_hash(hashed_pw, 'password')
# False
# >>> bcrypt.check_password_hash(hashed_pw, 'testing')
# True
# >>>


