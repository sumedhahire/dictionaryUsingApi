function emptyCheck(){
    var value=document.getElementById("para").value
    if(value==""){
        document.getElementById("info").innerHTML="Text cannot be empty"
    }
}

function reset(){
    document.getElementById("para").value=""
}