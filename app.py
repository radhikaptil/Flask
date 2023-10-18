from flask import Flask,render_template

FAI=Flask(__name__)


#response in the form of string.
@FAI.route('/wish')
def wish():
    return '<center><h1>Hey Good Morning</h1></center>'


#Collecting the data that coming from url.
@FAI.route('/data/<name>')
def data(name):
    return f'Hi {name} How are you'


#returning html page
@FAI.route('/first')
def first():
    return render_template('first.html',name='Radhika')


@FAI.route('/second')
def second():
    return render_template('second.html')


#Changing host and port number
if __name__=='__main__':
    FAI.run(debug=True,host='192.168.1.11',port=8000)


