function loginvalid(){
var xyz=document.getElementById("uname").value;
var pwo=document.getElementById("upass").value;
if(xyz!="" && pwo!=""){
alert("You are logged in as "+xyz)
}
else
alert("WRONG ENTRY!!")
}
function signupvalid(){
var $x=document.getElementById("fname").value;
var $y=document.getElementById("email").value;
var $z=document.getElementById("lname").value;
var $Sp=document.getElementById("signpass").value;
if($x!="" && $z!="" && $y!="" && $Sp!="")
alert("You are Signed in by using Email ID:"+$y+" and Your name as "+$x+" "+$z)
/*if($x!="" && $z!="" && $y!="" && $Sp!=""){
    alert("You are Signed in by using Email ID:"+email+" and Your name as "+fna)
}*/
else
alert("WRONG ENTRY!!")
}
