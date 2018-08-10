# jyang-sandbox
 This is a serverless blog powered by Hugo! Write markdowns, enjoy them as html pages!
 Some cool features:
* S3 serverless hosting
* Cloudfront as CDN
* SSL enabled!
* CircleCI deployment!
 Some bugs I'm still working on:
* Lambda/APIGateway handling the Contact form
 The following is included with the cloudformation:
* Lambda IAM role with SES SendEmail policy
* S3 bucket to host website
* Cloudfront configured with SSL
* Contact form Lambda
* API Gateway POST method for Contact form lambda (Broken)
 ### How to deploy:
 Simply deploy the included cloudformation template with the following parameter overrides:
* BlogBaseName: What you would like to name your blog
* ContactReceiverEmail: The Contact form response receiver email address
* ContactSenderEmail: The Contact form response sender email address
 ```
aws cloudformation deploy \
  --template-file ./aws/cloudformation/nimbusblog.yml \
  --stack-name your-stack-name \
  --parameter-overrides \
    BlogBaseName=yourblogname \
    ContactReceiverEmail=YourContactReceiverEmail@biz.co \
    ContactSenderEmail=YourContactSenderEmail@biz.co \
  --capabilities CAPABILITY_NAMED_IAM
  ```
