let orderButtons = document.getElementsByClassName("basket-button")

for (let i = 0; i < orderButtons.length; i++){              //for every orderButton create a click event
    orderButtons[i].addEventListener('click', function(){
        let articleID = this.dataset.article;       //this is the object that was clicked, dataset refers to the data-article to get the article.id
        let action = this.dataset.action;
        //alert('ArtikelID: '+articleID + "Aktion" + action)
    })

}