# jyang-sandbox
 This is a serverless blog powered by Hugo! Write markdowns, enjoy them as html pages!
 Some cool features:
* S3 serverless hosting
* Cloudfront as CDN
* SSL enabled!
* CircleCI deployment!

The following is included with the cloudformation:
* Lambda IAM role with SES SendEmail policy
* S3 bucket to host website
* Cloudfront configured with SSL
* Contact form Lambda
* API Gateway POST method for Contact form lambda
 ### How to deploy:
 
 #### Via Cloudformation/AWS cli
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
  
  #### Via CircleCI
  Simply clone or fork this project and build this on your own CircleCI instance!
  
  You will need the following environment variables set in your project settings or the build will fail:
  
  ```
  BLOGBASE: What you would call your blog (domain name without .com)
  RECEIVER_EMAIL: The email of the recipient for the contact forms (probably yourself)
  SENDER_EMAIL: The email of the sender for the contact forms (whatver you registered in SES)
  AWS_REGION: The AWS region you are deploying your blog
  S3_BLOG_BUCKET: The S3 Bucket name for your blog files (BLOGBASE + .com)
  S3_RESOURCE_BUCKET: The S3 Bucket for your other files (we are keeping lambda packages here)
  HUGO_BUILD_DIR: The build directory for Hugo. Default is ~/hugo
  ```
