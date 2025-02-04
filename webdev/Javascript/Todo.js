
function addtask(){

var data = '<span class="input-group-text">#</span><input type="text" class="form-control input-group" id="newtaskname" readonly><button class="btn btn-danger" onclick="removetask()">X</button><button class="btn btn-warning" onclick="displaytask()">Display</button>';

document.getElementById("newtask").innerHTML = data;

var name = document.getElementById("taskname").value;

document.getElementById("newtaskname").value = name;

}


function removetask(){

document.getElementById("newtask").innerHTML = "";

document.getElementById("displaydiv").style.display = "none";
}

function edittask(){

var editeddata = '<span class="input-group-text">#</span><input type="text" class="form-control input-group" id="newtaskname"><button class="btn btn-danger" onclick="removetask()">X</button><button class="btn btn-warning" onclick="displaytask()">Display</button>';

document.getElementById("newtask").innerHTML = editeddata;

var name = document.getElementById("taskname").value;

document.getElementById("newtaskname").value = name;

}

function displaytask(){

var name = document.getElementById("newtaskname").value;

document.getElementById("displaycontent").innerHTML = name;

if (name != "") {
document.getElementById("displaydiv").style.display = "block";
}

}
