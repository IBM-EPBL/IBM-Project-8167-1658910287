from flask import Flask, redirect, render_template, request

app = Flask(_name_)

@app.route('/', methods=['GET'])
def index ():
  #Home page
  return render_template("template.html")

  @app.route('/predict', methods =['GET','POST'])
  def upload ():
    # logic yet to be build 
    if request.method == 'GET':
      return ("Here the logic is defined")
    if request.method == 'POST':
      return ("Here the logic is defined")
  if_name_ == '_main_':
      app.run()