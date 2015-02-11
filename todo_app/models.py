from sqlalchemy import Column, Integer, String, Date, Boolean, Float, Enum, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from todo_app import db

class LoginModel(db.Model):
	""" model for login which store user credentials"""

	__tablename__ = "users"

	id = Column(Integer, primary_key = True)
	email_id = Column(String(50)) # user email id
	password = Column(String(64)) # hashed with md5

	def __repr__(self):
		return '<User %r>' % (self.email_id)

	def save(self):
		db.session.add(self)

class TaskBoard(db.Model):
	"""User's details about assiging task, deletijng task,.etc"""

	__tablename__ = "user_tasks"

	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey("users.id"), index = True)
	users = relationship("LoginModel")
	task_name = Column(String(70))
	description = Column(String(200))
	start_date = Column(Date)
	end_date = Column(Date)

	def __repr__(self):
		return '<DashBoard %r>' % (self.user_id)

	def save(self):
		db.session.add(self)

class ShareModel(db.Model):
	"""User's shared tasks"""

	__tablename__ = "shared_tasks"

	id = Column(Integer, primary_key = True)
	task_id = Column(Integer, ForeignKey("user_tasks.id"))
	task = relationship("TaskBoard")
	shared_by = Column(String(50))
	shared_to = Column(String(50))

	def __repr__(self):
		return '<ShareModel %r>' %(self.task_id)

	def save(self):
		db.session.add(self)

def commit():
	db.session.commit()
