### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



## Variable Rule
@app.route('/success/<score>') # 33 + 33 = 3333 , 33 + 33 = 66 , int(abc) > 50
def success(score):
    print("score type",type(score))
    res=""
    
    if int(score)>=50:
        res="PASSED"
    else:
        res="FAILED"

    # return ("the score input was: ",score) # this does not work in html, the score will not get printed
    # return ("the score input was: "+ score)
    # return ("the score input was: "+ res)
    return render_template('result.html',results=res)

#############
@app.route('/num/<int:myscore>') # Give an int value here
def num(myscore):
    print("num type",type(myscore))
    res=""
    
    if myscore>=50:
        res="PASSED"
    else:
        res="FAILED"

    # return ("the score input was: ",score) # this does not work in html, the score will not get printed
    # return "the num input was: "+ str(myscore)
    return render_template('result.html',results=res)

## Variable Rule
@app.route('/successres/<int:score>') # successres , score
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score':score,"res":res}

    return render_template('result1.html',results=exp)

# ## if confition
# @app.route('/sucessif/<int:score>')
# def successif(score):

#     return render_template('result.html',results=score)

# @app.route('/fail/<int:score>')
# def fail(score):
#     return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET']) # http://localhost:5000/submit
def submit():
    total_score=0
    if request.method=='POST': # if its a GET request then it will be false
        science     =float(request.form['science'])
        maths       =float(request.form['maths'])
        c           =float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score)) # got to successres , score

if __name__=="__main__":
    app.run(debug=True)

