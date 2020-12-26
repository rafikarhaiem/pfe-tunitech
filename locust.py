import re
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
  def on_start(self):
    self.login()

  def login(self):
    response = self.client.get("/login")
    print("Content: ", response.content)
    csrftoken = re.search('meta name="csrf-token" content="(.+?)"', response.text).group(1)

    print("token: ", csrftoken)
    post_data = {'email': "rafika@gmail.com", 'password': '123456', "_token": csrftoken }
    with self.client.post('/login', post_data,
                catch_response=True) as response:
      print("Code: ", response.status_code)
      print("Content: ", response.content)


  @task()
  def index(self):
    self.client.get("/")
  @task()
  def index(self):
    self.client.get("/home")

class WebsiteUser(HttpLocust):
  task_set = UserBehavior
  min_wait = 5000
  max_wait = 9000
