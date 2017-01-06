import re , datetime 
from app import app , db 

def slugify(s):
	return re.sub('[^\w]+','-',s).lower()
post_tags = db.Table('post_tag',
	            db.Column('tag_id' , db.Integer , db.ForeignKey('tag.id')),
	            db.Column('post_id',db.Integer , db.ForeignKey('posts.id')))
class Posts(db.Model):
	STATUS_PUBLIC = 0
	STATUS_DRAFT = 1
	id = db.Column(db.Integer , primary_key=True)
	title = db.Column(db.String(200))
	slug = db.Column(db.String(100), unique=True)
	body = db.column(db.Text)
	status = db.Column(db.SmallInteger , default=STATUS_PUBLIC)
	created_timestamp = db.Column(db.DateTime , default=datetime.datetime.now)
	modified_timestamp = db.Column(db.DateTime , default=datetime.datetime.now , onupdate=datetime.datetime.now)
	tags  = db.relationship('Tag' , secondary=post_tags , backref=db.backref('Posts' , lazy='dynamic'))
	def __init__(self , *args , **kwargs):
		super(Posts , self).__init__(*args , **kwargs) #call current constructors 
		self.generate_slug()
	def generate_slug(self):
		self.slug = ''
		if self.title:
			self.slug = slugify(self.title)
	def __repr__(self):
		return '<Post : %r>' % self.title
class Tag(db.Model):
	id = db.Column(db.Integer , primary_key=True)
	name = db.Column(db.String(64))
	slug = db.Column(db.String(64) , unique=True)
	def __init__(self , *args , **kwargs):
		super(Tag , self).__init__(*args , **kwargs) #call the current constructor 
		self.slug = slugify(self.name)
	def __repr__(self):
		return '<Tag  : %r>' % self.name 
