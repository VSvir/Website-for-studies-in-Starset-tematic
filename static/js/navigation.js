let inner_text = document.title
console.log("inner_text:", inner_text)
document.getElementById("navbarNavAltMarkup").hidden = 1

a_collection = document.getElementsByClassName("nav-link")
for (let index = 0; index < a_collection.length; index++) {
    console.log('')
    console.log(a_collection[index])
    if (a_collection[index].innerText === inner_text) {
        a_collection[index].className = 'nav-link active'
        console.log(a_collection[index].id)
    }
}