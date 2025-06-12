# Topics Covered: 
- AWS Snowball 
- AWs lambda 
- Event notification service
- Life cycle rules 
- EC2 storage
- Snapshots
-


# AWS Snowball
AWS Snowball is a physical data transfer service designed to move large amounts of data into and out of AWS efficiently. It is part of the **AWS Snow Family**, which also includes **AWS Snowcone** and **AWS Snowmobile**.  

### **Key Features of AWS Snowball:**  
1. **Data Migration & Transfer:**  
   - Ideal for transferring petabytes of data when internet-based transfer is too slow or costly.  
   - Helps migrate data to Amazon S3, Glacier, or other AWS storage services.  

2. **Two Variants:**  
   - **Snowball Edge Storage Optimized**:  
     - 80 TB usable storage (HDD-based).  
     - Best for bulk data transfer and storage-heavy workloads.  
   - **Snowball Edge Compute Optimized**:  
     - 42 TB usable storage (SSD-based).  
     - Includes **AWS Greengrass**, EC2, and Lambda for edge computing.  

3. **Security:**  
   - Encrypted with **256-bit encryption**.  
   - Uses **TPM (Trusted Platform Module)** for hardware security.  
   - Data automatically erases after transfer.  

4. **Edge Computing Capabilities:**  
   - Can run **EC2 instances** and **Lambda functions** on the device.  
   - Useful for **remote locations** where cloud connectivity is limited.  

5. **Use Cases:**  
   - **Data center migration** (moving large datasets to AWS).  
   - **Disaster recovery** (quickly backing up large volumes of data).  
   - **Edge computing** (processing data locally before sending it to AWS).  
   - **Content distribution** (delivering preloaded data to remote locations).  

### **How It Works:**  
1. **Order a Snowball** via AWS Console.  
2. AWS ships a **ruggedized appliance** to your location.  
3. You **connect the device** to your local network and transfer data.  
4. Once done, ship it back to AWS (prepaid shipping label included).  
5. AWS **uploads the data** to your S3 bucket.  




# AWS Lambda 
- Defining function with events, triggers and context. 
- Serverless Service 
- Run code without managing servers
- Triggered when something occurs (upload to s3, API request, Database entry is updated)
- functions can be scheduled or event based

### Example usage of Lambda
- Creating a notification service for whenever a file is uploaded to S3 bucket or something else
- Create a lambda function
- Go to bucket and create an event notification service and select the created lambda function 
- The print statements in the function will push the outputs to a log file which can be accessed using cloud watch.

```
import json

def lambda_handler(event, context):
    print("Event Received:", json.dumps(event, indent=4))
    
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        print(f"New file uploaded: s3://{bucket_name}/{object_key}")

    return {"status": "Success"}
```

# Life cycle rule
- It is usefull to use lifecycle rules to manage objects in a bucket
- Example usage: moving non current versions to a glacier storage class
- Example usage: deleting records automatically after a certain duration 

# EC2 instance storage types:
### volumes (EBS): 
- you can create a volume in the same region as your instance and connect your instance to created volume. 
- Needs to be in the same AZ
### elastic file storage (EFS):
- can create an efs storage in any az and connect from any az 
- needs to in the same region
- slower than ebs
- Expensive 
- pay per use 
- No storage planning
### Instance storage:
- Connected to the instance directly (like on the same pcb)
- Deleted when instance is deleted (Ephemeral)
- Expensive 
- Fastest
- used for buffering, caching, temporary data etc. 

## Snapshots: 
- One can create disk snapshots that can be restored in any az, any region. 
- can be useful when deleting a volume/efs that needs to be loaded back in the future. 
