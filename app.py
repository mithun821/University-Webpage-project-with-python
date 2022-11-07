from os import error
from flask import Flask ,render_template,request,redirect, url_for, session,flash
 #from flask_mail import Mail, Message

# from form_contact import ContactForm, csrf

# mail = Mail()

import mysql.connector

import re
  
app = Flask(__name__) #creating the Flask class object 
app.secret_key="mithun"
# mail=mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mithunerror@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sdatabase"
)

mycursor=conn.cursor()


@app.route('/') #decorator drfines the   
def index():  
    return render_template("index.html")


@app.route('/eu_profile') #decorator drfines the   
def eu_profile():  
    return render_template("eu_profile.html")


@app.route('/authority') #decorator drfines the   
def authority():  
    return render_template("authority.html")   

@app.route('/trusty') #decorator drfines the   
def trusty():  
    return render_template("trusty.html")

@app.route('/bba') #decorator drfines the   
def bba():  
    return render_template("bba.html")  

@app.route('/law') #decorator drfines the   
def law():  
    return render_template("law.html")  

@app.route('/llb') #decorator drfines the   
def llb():  
    return render_template("llb.html")  


@app.route('/eng') #decorator drfines the   
def eng():  
    return render_template("f_eng.html")  

@app.route('/cse') #decorator drfines the   
def cse():  
    return render_template("cse.html")   


@app.route('/tution') #decorator drfines the   
def tution():  
    return render_template("tution.html")              

@app.route('/admission_in') #decorator drfines the   
def admission_in():  
    return render_template("admission_in.html")


@app.route('/blog') #decorator drfines the   
def blog():  
    return render_template("blog.html")




@app.route('/contact') #decorator drfines the   
def contact():  
    return render_template("contact.html")


@app.route('/atth') #decorator drfines the   
def atth():  
    return render_template("atth.html")

@app.route('/view') #decorator drfines the   
def view():  
    return render_template("campus.html")

@app.route('/course') #decorator drfines the   
def course():  
    return render_template("course.html")


 
@app.route('/login') #decorator drfines the   
def login():  
    return render_template("s_login.html")

@app.route('/f_login') #decorator drfines the   
def f_login():  
    return render_template("f_login.html")

@app.route("/login_validation",methods=['GET','POST'])
def login_validation():
    error=None;
    userid=request.form.get("userid")
    userpass=request.form.get("userpass")
    mycursor.execute("""SELECT * FROM `stable` WHERE `my_id` LIKE'{}' and `pass` LIKE'{}'""" .format(userid,userpass))
    # mycursor.execute('SELECT * FROM stable WHERE my_id = % s AND pass = % s', (userid,userpass,))
    #mycursor.execute("SELECT * FROM stable where user_id='" +userid+"' and password='"+userpass+"'")
   # mycursor.execute("SELECT * FROM stable")
    users=mycursor.fetchall()
    print(users)
    
    # if users is not None:
           
    #       if users['userid']==userid and users['userpass']==userpass:
    #            return render_template("s_profile.html")
            
    
       
    #       else:
    #          return "unsucces"  

  
   
    if len(users)>0:
       

        return render_template("s_profile.html")
    else:
        error="invaild password"
        flash=('invaild userid or password')
        
        return redirect(url_for("login"))

# faculty login backend  
@app.route("/flogin",methods=['GET','POST'])
def flogin():
    error=None;
    userid=request.form.get("userid")
    userpass=request.form.get("userpass")
    mycursor.execute("""SELECT * FROM `ftable` WHERE `f_id` LIKE'{}' and `f_pass` LIKE'{}'""" .format(userid,userpass))
   
    users=mycursor.fetchall()
    print(users)
    
       

  
   
    if len(users)>0:
       

        return 'faculty login succesfully'
    else:
        error="invaild password"
        
        return redirect(url_for("f_login"))


@app.route('/logout') #decorator drfines the   
def logout():
    session.pop('userid',None)  
    return redirect(url_for("index"))     



@app.route('/register') #decorator drfines the   
def register(): 


  return render_template("register.html")
  
@app.route('/registers',methods=["GET","POST"])
def registers():
  error=None;
   
  
  my_id=request.form.get("my_id")
  pwss=request.form.get("pwss")      
 
  name=request.form.get("name")

  mycursor.execute("insert into stable(my_id,pass,name)values(%s,%s,%s)",(my_id,pwss,name))
  # mycursor.execute("""insert into  `stable` (`my_id`,  `pass`,`name`)values('{}','{}','{}')'""" .format(my_id,pwss,name))
  conn.commit()
        
  return "register succesfull"



@app.route('/contact', methods=['POST', 'GET'])
def contactf():
    form = ContactForm()
    if form.validate_on_submit():        
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])       
        print('-------------------------')
        send_message(request.form)
        return redirect('/success')    

    return render_template('views/contacts/contact.html', form=form)

@app.route('/success')
def success():
    return render_template('views/home/index.html')

def send_message(message):
    print(message.get('name'))

    msg = Message(message.get('subject'), sender = message.get('email'),
            recipients = ['mithunerror@gmail.com'],
            body= message.get('message')
    )  
    mail.send(msg)



if __name__ =='__main__':  
   app.run(debug = True)       