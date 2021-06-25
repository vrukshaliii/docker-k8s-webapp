function startDocker() {

    var i = document.getElementById("in1").value;
    var j = document.getElementById("in2").value;

    var xhr = new XMLHttpRequest();
    xhr.open("GET", `http://54.82.110.39/cgi-bin/docker.py?osname= ${i}&osimage= ${j}`, true);
    xhr.send();

    xhr.onload = function() {
        document.getElementById("out").innerHTML = xhr.responseText;
    }
}

function stopDocker() {

    var k = document.getElementById("in3").value;

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://54.82.110.39/cgi-bin/stop.py?stop_os_name=" + k, true);
    xhr.send();

    xhr.onload = function() {
        document.getElementById("out").innerHTML = xhr.response;
    }
}

function delDocker(){

    var l = document.getElementById("in4").value;

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://54.82.110.39/cgi-bin/del.py?del_os_name=" + l, true);
    xhr.send();

    xhr.onload = function() {
        document.getElementById("out").innerHTML = xhr.response;
    }
}

function dockerInfo(){

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://54.82.110.39/cgi-bin/info.py", true);
    xhr.send();

    xhr.onload = function() {
        document.getElementById("out").innerHTML = xhr.responseText;
    }
}

function listImages() {

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://54.82.110.39/cgi-bin/listimg.py", true);
    xhr.send();

    xhr.onload = function() {
        document.getElementById("out").innerHTML = xhr.responseText;
    }
}

function listCont() {

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://54.82.110.39/cgi-bin/listcont.py", true);
    xhr.send();

    xhr.onload = function() {
        document.getElementById("out").innerHTML = xhr.responseText;
    }
}
function listAllCont() {

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://54.82.110.39/cgi-bin/allcont.py", true);
    xhr.send();

    xhr.onload = function() {
        document.getElementById("out").innerHTML = xhr.responseText;
    }
}

