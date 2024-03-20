# AWS-automated-photo-processing
### This is a simple Serverless Photo Processing Architecture that utilizes AWS Lambda and S3 for automated photo processing and Amazon SNS for notification delivery. By seamlessly integrating these services, users can upload photos, trigger processing tasks, and receive notifications about the processing status. This serverless approach offers scalability, flexibility, and cost-effectiveness, making it ideal for applications requiring efficient photo processing workflows without managing infrastructure.

![S3-Lambda-sns](https://github.com/Ashenafi-Godana/AWS-automated-photo-processing/assets/131515289/5abcd4da-b4ff-4425-9a87-465bddf2fcac)

## How it works

### 1. User Uploads Photo:
* The process begins when a user interacts with the user interface to upload a photo.
* The user could be using a web application, mobile app, or any other interface capable of uploading files.

### 2. Amazon S3 Photo Upload Event:

* When the user uploads a photo, the photo file is stored in an Amazon S3 bucket.
* Amazon S3 detects the upload event and triggers an event notification.

### 3. AWS Lambda Function Trigger:

* The S3 event notification triggers an AWS Lambda function.
* The Lambda function is configured to execute in response to the S3 event.

### 4. Photo Processing and Handling:

* Upon triggering, the Lambda function executes custom code to process the uploaded photo.
* Photo processing tasks could include resizing, cropping, adding watermarks, or any other desired manipulations.
* The Lambda function can access the uploaded photo from the S3 bucket, process it, and perform further actions.

### 5. Send Notification via Amazon SNS:

* After processing the photo, the Lambda function sends a notification using Amazon SNS.
* The notification could be a message indicating successful processing, details about the processed photo, or any other relevant information.
* Amazon SNS delivers the notification to subscribers, which could include email addresses, mobile devices, HTTP endpoints, or other AWS services.
* 
### 5. Completion:

* Upon completing the processing and notification tasks, the Lambda function execution finishes.
* The processed photo remains stored in the Amazon S3 bucket for further use or retrieval.
* The user may receive a notification indicating that the photo has been processed successfully.
