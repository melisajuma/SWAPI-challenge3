$( document ).ready(function(){
    $ajax({
        method:"GET",
        url: "https://swapi.co/api/people/",
        
    }).done(function(data){
        console.log(data)

    })
})
