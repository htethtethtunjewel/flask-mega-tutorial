from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
@app.route('/con')
def con():
    user={'username':'Htet'}
    posts=[
            {'author':{'username':'Htun'},
             'body':'Beautiful day in Porland!'},
            {'author':{'username':'Htoo'},
             'body':'The Avengers movie was so cool!'}
           ]
    return render_template('loop.html',title='Home',user=user,posts=posts)
if __name__=="__main__":
    app.run()

