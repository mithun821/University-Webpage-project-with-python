function my_function(){



    var x=document.getElementById("userpass")
    var y=document.getElementById("hiden1")
    var z=document.getElementById("hiden2")
    if(x.type==='password'){
        x.type="text";
        y.style.display=block;
        z.style.display=none;
    }
    else{
        x.type="password";
        y.style.display=none;
        z.style.display=block;
    }
    
    }


    function validate(){

       var userid=document.getElementById("user_id")
        var pass=document.getElementById("my_pass").value;


        if(userid.type==='2556' && pass.type==="1234" )
        {
            alert("Login succesfull");
            return false;
            
         
           



        }
         else{
             alert("user_id and password did not match") ;

         }
    }