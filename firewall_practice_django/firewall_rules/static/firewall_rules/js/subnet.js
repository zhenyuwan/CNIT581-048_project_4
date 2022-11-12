var esubnet_answer = "192.168.1.0/24"
var private_a_answer = "192.168.0.0/25"
var private_b_answer = "192.168.0.128/25"

if(!localStorage.getItem('esubnet')) {
  // if esubnet key is not found in the localstorage, call populateStorage
  populateStorage("esubnet","esubnet_result");
} else {
  // if esubnet key is found, call setStyles
  setStyles("esubnet","esubnet_result");
}

if(!localStorage.getItem('private_a')) {
  // if private_a key is not found in the localstorage, call populateStorage
  populateStorage("private_a","private_a_result");
} else {
  // if private_a key is found, call setStyles
  setStyles("private_a","private_a_result");
}

if(!localStorage.getItem('private_b')) {
  // if private_b key is not found in the localstorage, call populateStorage
  populateStorage("private_b","private_b_result");
} else {
  // if private_b key is found, call setStyles
  setStyles("private_b","private_b_result");
}

function populateStorage(key,element_id) {
  var key;
  var element_id;
  //save the current innerHTML of element subnet_result
  localStorage.setItem(key, document.getElementById(element_id).innerHTML);
  //call setStyles()
  setStyles();
}

function setStyles(key,element_id) {
  var key;
  var element_id
  // set the value of variable to be the value stored in the local storage
  var esubnet_text = localStorage.getItem(key);
  
  // assigne the value of variable to innterHTML of HTML element
  document.getElementById(element_id).innerHTML = esubnet_text;
  if (esubnet_text == "Correct"){
    // NOTE: the reason I am using key variable instead of element_id is the HTML element id
    // I want to change is the input box, whose id value is the same as key variable
    document.getElementById(key).style = "background-color:green";
  }else{
    document.getElementById(key).style = "background-color:red";
  }
}

function esubnet_result_validate() {
  result_validate("esubnet",esubnet_answer);

  //Save the text of esubnet element to local storage
  localStorage.setItem('esubnet',document.getElementById("esubnet_result").innerHTML);
}
function private_a_result_validate() {
  result_validate("private_a",private_a_answer);

  //Save the text of private a element to local storage
  localStorage.setItem('private_a',document.getElementById("private_a_result").innerHTML);
}
function private_b_result_validate() {
  result_validate("private_b",private_b_answer);
  //Save the text of private b element to local storage
  localStorage.setItem('private_b',document.getElementById("private_b_result").innerHTML);
}

function result_validate(element_id,answer) {

  if (document.getElementById(element_id).value == answer){
    document.getElementById(element_id+"_result").innerHTML = "Correct";
  }else{
    document.getElementById(element_id+"_result").innerHTML = "Try Harder";
  }
}
