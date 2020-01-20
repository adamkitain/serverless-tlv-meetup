
function repeatHttp(concurrency) {
    let count=0;
    setInterval(function () {
        for(i=0; i<concurrency; i++){
            count += 1;
            $.ajax({
                url: "http://internal-serverless-tlv-meetup-alb-393170614.us-east-1.elb.amazonaws.com/user/random",
                method: 'GET',
                cors: true
            }, function(data) {
                console.log(data);
            });
            console.log("Count is: ", count);
        };
    }, 3000)
}

 repeatHttp(3);