from flask import Flask ,render_template,request,redirect, url_for, session
import mysql.connector
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def login():  
    return render_template('')


@app.route('/result',methods=['POST',"GET"])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testdb"
    )
    mycursor=mydb.cursor()




        
        
        
    
    mycursor=mydb.cursor()
    if request.method=="POST":
        signup=request.form
        user=signup["user_id"]
        password=signup["password"]
        mycursor.execute("SELECT * FROM info where user_id='" +user+"' and password='"+password+"'")
        r=mycursor.fetchall()
        count=mycursor.rowcount
        if count==1:
            return "succes"
        elif count>1:
            return 'flse'

        else:
            return "not true"   


    mydb.commit()
    mycursor.close()

  
if __name__ =='__main__':  
   app.run(debug = True)      

      
  
