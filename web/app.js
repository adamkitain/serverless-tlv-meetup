
function repeatHttp(concurrency) {
    let count=0;
    setInterval(function () {
        for(i=0; i<concurrency; i++){
            count += 1;
            $.ajax({
                url: "/test",
                method: 'GET',
                success: function(data) {console.log(data);}
            });
            console.log("Count is: ", count);
        };
    }, 3000)
}

// repeatHttp(2);