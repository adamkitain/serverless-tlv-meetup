# Serverless TLV Meetup
## _January 21, 2020_

AWS Lamda has, in many ways, replaced conventional servers. The databases they work with, though, haven't changed all that much. 
This talk covers best practices, tips, and tricks for getting your Lambdas to play nicely with your databse.

### Topics Covered
* Serverless Framework
* AWS Secrets Manager
* Connecting to the Database
* Preventing Choking the DB 
* Monitoring (CloudWatch + Epsagon)

### Running the code
To deploy your code to your AWS account
```
$ npm install -g serverless
$ sls deploy --region us-east-1 
```

To run the web demo:
```
$ cd web/
$ python -m SimpleHTTPServer
$ open http://localhost:8000/index.html
```