# from flask import Flask
# from flask import Flask, render_template # is used to use html tempaltes or files
from flask import Flask, render_template, url_for, request, redirect 
import csv
app = Flask(__name__)
# print(__name__)

@app.route('/')
# def hello_world():
def my_home():
    # return 'Hello, Azizullah Mahjoor, A test for your project'
    # return render_template('index.html') # this gives us an error because flask look after templates folder then html file.
    #so we need to Move the index.html file into templates folder
    return render_template('index.html') #but the css and JS file is still no working, So we need to creat a folder (static) and copy both into static folder and in index.html file set path as static/style.css and static/script.js to load
    #in CMD: if we wnat to run this file via server so we need to run the server
    #to run the flask framework for running server we need to try this command
    #Go to you project via "cd" and then, activate the virtual environment.
    #>Desktop>web_server\Scripts\activate.bat
    # now, cd web_server
    #~Desktop>web_server>set FLASK_APP=server.py(the file name)
    # now, C:\Users\Mahjoor\Desktop>web_server\Scripts\activate.bat
    #(web_server) C:\Users\Mahjoor\Desktop>cd web_server
    #(web_server) C:\Users\Mahjoor\Desktop\web_server>set FLASK_APP=server.py
    #(web_server) C:\Users\Mahjoor\Desktop\web_server>flask run
    # the above commands are using to run flask but in debugger mode = off means it needs to run again flask run command for every changes
    
    #if you want to run flask with debugger mode = ON, so we need to run the following commands
    #(web_server) C:\Users\Mahjoor\Desktop\web_server>set FLASK_DEBUG=1  (this command is used to not run flask again for every changes in file.)
    #(web_server) C:\Users\Mahjoor\Desktop\web_server>flask run
    #http://127.0.0.1:5000 -> the server is running of this port
    
# @app.route('/index.html')
# def home():
#     return render_template('index.html')  
    

# @app.route('/blog.html')
# def blog():
#     return render_template('blog.html')  
    
   
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')  
    

# @app.route('/furniture.html')
# def furniture():
#     return render_template('furniture.html')  
    

# @app.route('/about.html')
# def about():
#     return render_template('about.html')  

 
# if we look at the above for every URL we have created a function it is repeated work. just one function does that.
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)  

# def write_to_file(data):
#     with open('web_server/database.txt', mode='a') as database:
#         name = data['name']
#         number = data['number']
#         email = data['email']
#         message = data['message']
#         file = database.write(f'\n{name}, {number}, {email}, {message}')
    

def write_to_csv(data):
    with open('fortfo/database.csv', mode='a', newline='') as csv_database:# newline='' is used to have a new record in new line of CSV file
        name = data['name']
        number = data['number']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(csv_database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, number, email, message])
        
@app.route('/form_submit', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)# to see our data in cmd
            # write_to_file(data)
            write_to_csv(data)
            # return render_template('contact.html', name=name)
            return redirect('contact.html')
            # return 'Data submitted Successfuly'
        except:
            return 'did not save to database'
    else:
        return 'some thing went wrong. try again'
  
@app.route('/blog')
def blog():
    return 'these are my thoughts of blogs'


# @app.route('/<username>/<int:post_id>') # if we search with root a name and print it for us.
# def ReturnName(username=None, post_id=None):
#     return render_template('test.html', name=username, post_id=post_id) # name is the variable in html file
