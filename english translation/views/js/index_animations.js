function load_page(){
    let login_container = document.getElementsByClassName("login_container");
    login_container[0].style.height = "80vh";
    login_container[0].style.transition = " all 3s";
}

function new_container_anim(status){
    if(status == "open"){
        let login_container = document.getElementsByClassName("login_container");
        let new_container = document.getElementsByClassName("new_register_container");
        login_container[0].style.height = "0vh";
        new_container[0].style.width = "60%";
        login_container[0].style.transition = " all 3s";
        new_container[0].style.transition = " all 3s";
    }
    if (status == "close"){
        let login_container = document.getElementsByClassName("login_container");
        let new_container = document.getElementsByClassName("new_register_container");
        login_container[0].style.height = "80vh";
        new_container[0].style.width = "0%";
        login_container[0].style.transition = " all 3s";
        new_container[0].style.transition = " all 3s";
    }   
}

function recovery_pass(status){
    if(status == "open"){
        let login_container = document.getElementsByClassName("login_container");
        let recovery_container = document.getElementsByClassName("recovery_container");
        login_container[0].style.opacity = "0";
        recovery_container[0].style.opacity = "1";
        recovery_container[0].style.zIndex = "2";
        login_container[0].style.transition = "all 2s";
        recovery_container[0].style.transition = "all 2s";
    }
    if(status == "close"){
        let login_container = document.getElementsByClassName("login_container");
        let recovery_container = document.getElementsByClassName("recovery_container");
        login_container[0].style.opacity = "1";
        recovery_container[0].style.opacity = "0";
        recovery_container[0].style.zIndex = "-2";
        login_container[0].style.transition = "all 2s";
        recovery_container[0].style.transition = "all 2s";
    }
}