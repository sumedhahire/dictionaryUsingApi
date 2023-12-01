function emptyCheck(){
    var val=document.getElementById("para").value;
    console.log(val)
    if(val==""){
        document.getElementById("info").innerHTML="Text cannot be empty"
        window.history.forward(-1);
    }
}

function reset(){
    document.getElementById("para").value=""
}

function send(val){
    document.getElementById("para").value=val;
}