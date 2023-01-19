from flask import Blueprint
from . import db
from .models import Category, Product

bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    category1 = Category(name='Origami Crafts', image='animal.jpg', \
        description='''This is a great introductory product. You can buy a completed origami crafts for an affordable price. It can be used to decorate your room, as a gift to your friends, or taken apart to learn how to fold it. Our selection ranges from simple origami crafts that are easy for children to make, and to full-fledged pieces that adults can also enjoy.''')
    category2 = Category(name='Origami Papers', image='chiyogami.jpg', \
        description='''If you want to create your own original art piece, choose this product. There are many variations kinds of origami papers, from simple monochromatic origami paper to beautiful origami with traditional Japanese patterns which is so-called "Chiyogami". We also carry large-sized paper for those who want to create dynamic works.''')
    category3 = Category(name='Origami Tutorials', image='howtokangaroo.png', \
        description='''Are you struggling with origami folding? Try this tutorial booklet! Every sinle step is explained in detail, so even beginners can easily learn the basics of origami folding. The booklet is available in both English and Japanese, so it can be useful when folding with friends overseas.''')
      
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

#product data for db
    p1 = Product(category_id=category1.id, image='animal.jpg', price=4.99,\
        quantity='20 piece',\
        name='Simple Origami',\
        description= '[Content: 20 pieces] Simple origami works, including modular origami. These works are already completed and you can appreciate the beautiful works of origami as soon as the product arrives. This product can be widely used as interior decoration, as a gift, as a trinket for children, and as a teaching tool to learn how to fold. We randomly pack a variety of different types of pieces. You can also request the colors and types from the checkout form, if you want.') 
    p2 = Product(category_id=category1.id, image='compute.png', price=10.50,\
        quantity='10 papers',\
        name='Computational Origami',\
        description= '[Quantity: 10 pieces] Computer origami is the most advanced form of origami. Origami is not only for fun, but is also used by NASA and others as a technology for space exploration. This origami is designed by computer software and has succeeded in creating novel shapes that have never been seen before. It will be a wonderful and modern interior decoration for your room.')
    p3 = Product(category_id=category1.id, image='senbazuru.jpg', price=30.45,\
        quantity='1000 piece',\
        name='Thousand Origami Cranes',\
        description= '[Quantity: 1000 piece] The crane in Japan is one of the mystical or holy creatures and is said to live for a thousand years. Therefore, it is believed that if you got this, you are granted happiness and eternal good luck,  and also long life or recovery from illness or injury. This makes them popular gifts for special friends and family.')
    p4 = Product(category_id=category2.id, image='paper.jpg', price=9.99,\
        quantity='200 papers',\
        name='Simple Colors',\
        description= '[Quantity: 200 piece] Simple, single colored origami. Ideal for beginners. It comes in a variety of colors, so you can make your own origami creations with your favorite colors. Large quantity of 200 sheets!')
    p5 = Product(category_id=category2.id, image='chiyogami.jpg', price=10.55,\
        quantity='100 papers',\
        name='Chiyogami',\
        description= '[Quantity: 100] This is a beautiful kimono-like origami paper with traditional Japanese patterns. You can enjoy it as it is. It is a little thicker and sturdier than ordinary origami. When glued on a small box, it makes a very nice treasure box!')
    p6 = Product(category_id=category2.id, image='large.jpg', price=20.25,\
        quantity='50 papers',\
        name='Large-sized Papers',\
        description= '[Quantity: 50] Want to make a larger origami piece? Then you should try this product. Make big, dynamic creations like dragons and dinosaurs that in our showcase on the top page, and wow everyone!')
    p7 = Product(category_id=category3.id, image='booken.jpg', price=3.00,\
        quantity='1 booklet',\
        name='Tutorial Booklet (in English)',\
        description= '[Quantity: 1, Language: English] First time to try origami? With this book, even a beginner will soon be able to make all sorts of origami artwork with ease! Every sinle step is explained in detail, so even beginners can easily learn the basics of origami folding.')
    p8 = Product(category_id=category3.id, image='bookjp.jpg', price=3.00,\
        quantity='1 booklet',\
        name='Tutorial Booklet (in Japanese)',\
        description= '[Quantity: 1, Language: Japanese] First time to try origami? With this book, even a beginner will soon be able to make all sorts of origami artwork with ease! Every sinle step is explained in detail, so even beginners can easily learn the basics of origami folding.')

    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.commit()
    except:
        return 'There was an issue adding a product in dbseed function'

    return 'DATA LOADED'


