function sendMail(params){
    var tempParams={
        from_name:document.getElementById("fromName").value,
        email:document.getElementById("email").value,
        message:document.getElementById("msg").value,
    };

    emailjs.send('service_vad8bog','template_7kc85r2',tempParams)
    .then(function(res){
        console.log("success",res.status);
    })
}
function sendAlert(){
    alert("Your Data has been saved Sucessfully!")
    alert("Your Campaign will be add to our website in lessthan 72 hours while the reason and Given Details are the True")
}