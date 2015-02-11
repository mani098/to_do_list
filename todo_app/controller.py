from models import LoginModel, TaskBoard, db, commit
from flask import session
import hashlib, datetime
# from sqlalchemy import in_

class User:
	"""controller to handle all controls of todo list"""

	def login(self, email_id, password):
		"""logins the user if already exists or creates new row in users table for the new user"""

		password_hash = hashlib.md5(password)
		password = password_hash.hexdigest()

		try:
			user = db.session.query(LoginModel).filter(LoginModel.email_id == email_id).first()
			if user.email_id == email_id and user.password == password:
				return "success"
			elif user.email_id == email_id and user.password != password:
				return "Password is wrong"
		except:
			user = LoginModel()
			user.email_id = email_id
			user.password = password
			user.save()
			commit()
			return "success"

	def get_user_id(self, email_id):
		"""fetch the user id from db with the corresponding email_id"""
		user_id = db.session.query(LoginModel.id).filter(LoginModel.email_id == email_id).first()
		return user_id

	def create_task(self, user_id, task_name, desc, end_date):
		"""saves the newly created task"""

		task = TaskBoard()
		task.user_id = int(user_id)
		task.task_name = task_name
		task.description = desc
		task.start_date = datetime.date.today()
		task.end_date = datetime.datetime.strptime(end_date,'%m/%d/%Y').date()
		task.save()
		commit()

	def fetch_tasks(self, user_id):
		"""fetch the task created by a user"""
		data = db.session.query(TaskBoard).filter(TaskBoard.user_id == int(user_id)).all()
		return data

	def delete_tasks(self, task_ids):
		"""deletes the task based on the task_id """
		db.session.query(TaskBoard).filter(TaskBoard.id.in_(task_ids)).delete(synchronize_session='fetch')
		commit()

	def share_tasks(self, task_ids, shared_by, shared_to):
		pass

