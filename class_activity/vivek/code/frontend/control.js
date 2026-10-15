for(let i=0;i<3;i++){
    let line = "";
    for(let j=0;j<3;j++){
        line = line + "* " ;
    }
    console.log(line)
}

for(let i=1;i<=15;i++){
    if(i%3 == 0 && i%5 == 0){
        console.log("FizzBuzz");
    }else if(i%5 == 0){
        console.log("Buzz");
    }else if(i%3 == 0){
        console.log("Fizz");
    }
}