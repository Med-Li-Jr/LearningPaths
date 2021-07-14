let btnMenu = document.querySelectorAll(".btnMenu")
let sectionMenu = document.querySelectorAll(".sectionMenu")
let sectionLangEn = document.querySelectorAll(".eng")
let sectionLangFr = document.querySelectorAll(".fra")
let langNonActive = document.querySelectorAll(".langNonActive");

function showLanguagePart(index) {
   if(index===0){
        sectionLangFr.forEach(function (elt) {
            elt.style.display = "none";
        })
        sectionLangEn.forEach(function (elt) {
            elt.style.display = "block";
        })
    }
    else{
        sectionLangFr.forEach(function (elt) {
            elt.style.display = "block";
        })
        sectionLangEn.forEach(function (elt) {
            elt.style.display = "none";
        })
    }
    langNonActive.forEach(function (elt) {
        elt.classList.remove("langActive");
    })
    langNonActive[index].classList.add("langActive");
}

function showContentPart(index, indexFr) {
    btnMenu.forEach(function (elt) {
        elt.classList.remove("active");
    })
    sectionMenu.forEach(function (elt) {
        elt.style.display = "none";
    })
    sectionMenu[index].style.display = "unset";
    btnMenu[index].classList.add("active");
    btnMenu[indexFr].classList.add("active");
}

function increaseValue(idItems) {
    let inputElt = document.getElementById("input" + idItems);
    let currentValue = parseInt(inputElt.value);
    if (currentValue < parseInt(inputElt.max))
        currentValue++;
    inputElt.value = currentValue;
}

function decreaseValue(idItems) {
    let inputElt = document.getElementById("input" + idItems);
    let currentValue = parseInt(inputElt.value);
    if (currentValue > parseInt(inputElt.min))
        currentValue--;
    inputElt.value = currentValue;
}
function textInputChanges(idItems) {
    let inputElt = document.getElementById("input" + idItems);
    let currentValue = parseInt(inputElt.value);
    if (currentValue < parseInt(inputElt.min))
        currentValue = parseInt(inputElt.min);
    else if (currentValue > parseInt(inputElt.max))
        currentValue = parseInt(inputElt.max)

    inputElt.value = currentValue;
}

function getEltsChecked(name) {
    var ele = document.getElementsByName(name);

    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked)
            return ele[i];
    }
}
function calculMinute(){
    let hours = parseInt(document.getElementById("inputHours").value);
    let minutes = parseInt(document.getElementById("inputMinutes").value);
    let secondes = parseInt(document.getElementById("inputSecondes").value);

    hours = hours * 60;

    secondes = secondes > 30 ? 1 : 0;

    return ( hours + minutes + secondes );
}

function calculPriceTotal(){
    
  let totalPrice = 0.0;
  let rbServices = getEltsChecked('RbServices').value;
  let rbLang = getEltsChecked("RbLang").value;
  let totalMin = calculMinute();
  
  if(rbServices === "Normal")
    totalPrice = totalMin * 1;
  else
    totalPrice = totalMin * 1.5;
  
  if(rbLang !== "None")
    totalPrice += totalMin * 2;

    document.getElementById("priceValue").textContent = totalPrice;

}

