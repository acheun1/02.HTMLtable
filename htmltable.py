#Html Table
#2018 09 29
#Cheung Anthony

# When you build this, please make sure that your program meets the following criteria:

from flask import Flask, render_template
app = Flask(__name__)

#our index route will handle the form
@app.route('/')
def index():
    users = (
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    )
    cnt=len(users)
    return render_template('index.html', to_users=users, loopcnt=cnt)

if __name__=="__main__":
    app.run(debug=True)


