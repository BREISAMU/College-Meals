from flask import render_template, request, Blueprint
from src.models import Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    allPosts = Post.query.order_by(Post.date_posted.desc())
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, allPosts=allPosts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/Dessert")
def dessert():
    page = request.args.get('page', 1, type=int)
    allPosts = Post.query.order_by(Post.date_posted.desc())
    posts = Post.query.filter_by(type='Dessert').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('dessert.html', title='Dessert', posts=posts, allPosts=allPosts)

@main.route("/Breakfast")
def breakfast():
    page = request.args.get('page', 1, type=int)
    allPosts = Post.query.order_by(Post.date_posted.desc())
    posts = Post.query.filter_by(type='Breakfast').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('breakfast.html', title='Breakfast', posts=posts, allPosts=allPosts)

@main.route("/Lunch")
def lunch():
    page = request.args.get('page', 1, type=int)
    allPosts = Post.query.order_by(Post.date_posted.desc())
    posts = Post.query.filter_by(type='Lunch').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('lunch.html', title='Lunch', posts=posts, allPosts=allPosts)

@main.route("/Dinner")
def dinner():
    page = request.args.get('page', 1, type=int)
    allPosts = Post.query.order_by(Post.date_posted.desc())
    posts = Post.query.filter_by(type='Dinner').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    likes = Post.query.filter_by(id='2').first().title
    return render_template('dinner.html', title='Dinner', posts=posts, allPosts=allPosts)

@main.route("/Budget")
def cheap():
    page = request.args.get('page', 1, type=int)
    allPosts = Post.query.order_by(Post.date_posted.desc())
    posts = Post.query.filter_by(price='Cheap').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('cheap.html', title='Budget', posts=posts, allPosts=allPosts)


@main.route("/Budget-Breakfast")
def cheapBreakfast():
    page = request.args.get('page', 1, type=int)
    allPosts = Post.query.order_by(Post.date_posted.desc())
    posts = Post.query.filter_by(price='Cheap').filter_by(type='Breakfast').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('budget/cheapBreakfast.html', title='Budget Breakfast', posts=posts, allPosts=allPosts, typeCheck="Breakfast")

@main.route("/Budget-Lunch")
def cheapLunch():
    page = request.args.get('page', 1, type=int)
    allPosts = Post.query.order_by(Post.date_posted.desc())
    posts = Post.query.filter_by(price='Cheap').filter_by(type='Lunch').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('budget/cheapLunch.html', title='Budget Lunch', posts=posts, allPosts=allPosts, typeCheck="Lunch")

@main.route("/Budget-Dinner")
def cheapDinner():
    page = request.args.get('page', 1, type=int)
    allPosts = Post.query.order_by(Post.date_posted.desc())
    posts = Post.query.filter_by(price='Cheap').filter_by(type='Dinner').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('budget/cheapDinner.html', title='Budget Dinner', posts=posts, allPosts=allPosts, typeCheck='Dinner')

@main.route("/Budget-Dessert")
def cheapDessert():
    page = request.args.get('page', 1, type=int)
    allPosts = Post.query.order_by(Post.date_posted.desc())
    posts = Post.query.filter_by(price='Cheap').filter_by(type='Dessert').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('budget/cheapDessert.html', title='Budget Dessert', posts=posts, allPosts=allPosts, typeCheck="Dessert")

# @main.route("/Moderate")
# def lunch():
#     page = request.args.get('page', 1, type=int)
#     posts = Post.query.filter_by(price='Moderately priced').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
#     return render_template('moderate.html', title='Moderate', posts=posts)
#
# @main.route("/Expensive")
# def lunch():
#     page = request.args.get('page', 1, type=int)
#     posts = Post.query.filter_by(price='Expensive').order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
#     return render_template('expensive.html', title='Expensive', posts=posts)


