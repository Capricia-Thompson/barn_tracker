console.log("script loaded")
function showEmp() {
    document.querySelector("#cust").hidden = true
    document.querySelector("#emp1").hidden = false
}

function showCust() {
    document.querySelector("#cust").hidden = false
    document.querySelector("#emp1").hidden = true
}

function toggle_login() {
    if (document.querySelector('#login').hidden == true) {
        document.querySelector('#login').hidden = false
    } else if (document.querySelector('#login').hidden == false) {
        document.querySelector('#login').hidden = true
    }
}