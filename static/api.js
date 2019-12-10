const people=()=>{
    fetch("https://swapi.co/api/people/")
    .then((data)=>{
        let results=data.Results
        console.log(results)
    })
}

<<<<<<< HEAD
people()
=======
people()
>>>>>>> origin/master
