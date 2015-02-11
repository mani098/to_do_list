import os
from flask.ext.classy import FlaskView, route
from flask import Flask, request, flash, url_for, redirect, \
	 render_template, abort, send_from_directory, session


class LoginView(FlaskView):
	"""default login view for to-do-list"""

	@route('/')
	def index(self):
		return redirect(url_for("LoginView:login"))

	@route('/login/', methods=['POST', 'GET'])
	def login(self):
		message = ""
		if session.get("email_id"):
			return redirect(url_for('DashboardView:dashboard'))
		else:
			if request.method == "POST":
				email_id = request.form["email_id"]
				password = request.form["password"]
				from todo_app.controller import User
				login_status = User().login(email_id, password)
				if login_status == "success":
					session["email_id"] = email_id
					return redirect(url_for('DashboardView:dashboard'))
				else:
					message = login_status
					return render_template('login.html', message = message)

		return render_template('login.html', message = message)

	@route('/logout/')
	def logout(self):
		session.clear()
		return redirect(url_for("LoginView:login"))


class DashboardView(FlaskView):
	"""DashBoard for to-do-list where user create, delete tasks"""

	@route('/dashboard/', methods=['POST', 'GET'])
	def dashboard(self):
		if session.get("email_id"):
			from todo_app.controller import User
			email_id = session.get("email_id")
			user_id = User().get_user_id(email_id)
			test = "" #for testing purpose
			message, error = "", ""
			data = User().fetch_tasks(user_id[0]) #user's tasks
			if request.method == "POST":
				try:
					if request.form['new_task'] == "Create Task":
						test = request.form['new_task'] #forn testing purpose
						task_name = request.form['new_task_name']
						desc =  request.form['desc']
						end_date = request.form['end_date']
						if task_name and desc and end_date:
							User().create_task(user_id[0], task_name, desc, end_date)
							data = User().fetch_tasks(user_id[0])
							message = "Task Created successfully"
						else:
							error = "Sorry!, Task can't be created"
				except:
					if request.form['delete_task'] == "Delete Task":
						User().delete_tasks(request.form.getlist("mark_task"))
						data = User().fetch_tasks(user_id[0])

			return render_template('dashboard.html', email_id = email_id, test=test, \
								message = message, error = error, task_data = data)
		else:
			return redirect(url_for("LoginView:login"))


