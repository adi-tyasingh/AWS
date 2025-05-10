# Elastic Cloud compute   
          
Amazon Elastic Compute Cloud (EC2) is a web service offered by **Amazon Web Services (AWS)** that provides **resizable compute capacity** in the cloud. It allows users to run virtual machines, called **instances**, with varying configurations of CPU, memory, storage, and networking.  

## EC2 configs:
- OS -> (Linux, Windows, etc)
- CPU -> number of cores
- RAM -> amount of ram
- Storage -> type of storage(refer day 40)
- Network Card -> Public IP and speed of connection
- Firewall rules: security groups
- Bootstrap Script

## EC2 instance Types: 
**General purpose instances:**
- Good for general purpose tasks 
- Balance of compute, memory and storage.  

**Compute optimised:**   
- good for compute intensive tasks 
- Eg. dedicated gaming servers, HPC, Scientific computing.

**Memory Optimised:**  
- For memory intensive tasks 
- In memory databases, Apache spark, etc

**storage optimised:**   
- Tasks that require a large amount of storage

**Hardware Accelerated:**   
- Hardware accelerators are used to speed up tasks


## EC2 Purchasing options: 
**On demand instances:**
- Expensive
- Can be provisioned as needed. 
- Reliable (available till stopped/terminated)
- Ideal for short term, unstable(tasks that cannot be interrupted) tasks
- if need for Instance is short lived < 1 year. 

**Reserved Instances:**
- you can reserve an instance for 1 or 3 years. 
- Instance needs to be of a specific type, (Model, OS, region)
- Not very flexible
- best for when you know for a fact that you need a specific instance for a long period of time. 
- provides 3 payment option upfront, end, mixed. 
- Can be sold on AWS market place.

**Convertible Reserved Instances:**
- Similar to reserved instances. 
- provides option to change instance type, instance family, OS, tenancy and AZ. 
- much more flexible
- Ideal for when needs are unpredictable and may change
- cannot be sold on the market place.  

**Savings plans:**
- commitment to a certain spend per hour 
- bifurcated into 2 types 
- Compute Savings plan : allows to change region, instance family and more 
- EC2 savings plan : allows change in OS tenancy, but not in region and family. 
- Ideal when you dont want to commit to a specific type of instance.

**Spot Instances:**
- Ephemeral instances
- much cheaper than on demand instances
- sanctioned from spare capacity at AWS 
- Use a bidding system
- Can be withdrawn in case of increased demand or higher bid
- Useful for tasks that can be interrupted
- Cluster based tasks


**Dedicated Hosts:**
- Entire machine dedicated to you
- very expensive 
- useful for privacy compliancy laws and stuff 
- can direct instance placement

**Dedicated Instances:**
- VM is dedicated only to you and is not allocated to anyone else. 
- Cannot direct instace placement. 
- also very expensive


##  Storage Options: 
1. **Amazon Elastic Block Store (EBS)**
    - block storage 
    - Attached to single instance 
    - Supports encryption 
    - supports snapshots for backups
    - high performance
2. **Amazon Elastic File System (EFS)**
    - network storage 
    - can be attached to multiple instances 
    - supports encryption 
    - useful for when multiple instances need shared access to files 
    - works with linux instances
    - grows and shriks automatically
3. **Instance Store (Ephemeral Storage)**
    - very fast 
    - only works with one instance 
    - ideal for caching and high performace applications
    - low latency, high throughput
4. **Amazon Simple Storage Service (S3)**
    - buckets can also be used for storage
    - long term object storage solution

## Security 
following tools can be used to manage security of instances: 
- IAM roles
- Security groups(manage inbound and outbound traffic)(statefull and stateless)
- SSH methods (key pairs and instance connect)
- VPC (can be used to hide instance in a private subnet) 

## Networking
- Elastic IPs: Static IPs that can be reassigned to different instances.
- Amazon VPC (Virtual Private Cloud): Enables users to isolate networks.
- **Placement Groups**:
  - **Clustered**: Low-latency, high-bandwidth connections between instances.
  - **Spread**: Ensures instances are placed on separate hardware.
  - **Partitioned**: Used for distributed applications like Hadoop.

## Monitoring & Logging
- Amazon CloudWatch: Monitors CPU, memory, disk usage, and custom metrics.
- AWS CloudTrail: Logs all API requests to track security and compliance.


## EC2 Auto Scaling
- Dynamic Scaling: Adjust instances based on demand.
- Predictive Scaling: Uses machine learning to predict and scale in advance.

---

## Launching an Instance
1. Choose an **Amazon Machine Image (AMI)** (OS and pre-installed software).
2. Select **Instance Type** (CPU, RAM, etc.).
3. Configure **Security Groups**.
4. Assign an **SSH Key Pair** for secure access.
5. Attach **EBS Storage**.
6. Launch and connect using SSH or RDP.

## Connecting to an EC2 Instance
- **Linux:**   `ssh -i key.pem ec2-user@<public-ip>`
- **Windows:** Use RDP with credentials.

---

## Creating a Custom AMI
1. Configure an EC2 instance.
2. Create an **Image Snapshot** from the AWS console.
3. Deploy new instances using the custom AMI.

---

## Load Balancing
- Application Load Balancer (ALB): Routes traffic based on content type.
- Network Load Balancer (NLB): Handles high-performance TCP/UDP traffic.
- Classic Load Balancer (CLB): Legacy option for basic balancing.

---

## Advanced EC2 Features

- EC2 Image Builder: Automates the creation of AMIs with software patches and configurations.    
- Spot Fleets: Manage multiple Spot Instances for cost efficiency.   
- EC2 Bare Metal Instances: Provides direct hardware access for virtualization and containerization.   
- EC2 Nitro System: Provides better security, networking, and performance with hardware acceleration.   

---


## Common Use Cases
### Web Hosting
- Deploy scalable web applications (LAMP, MEAN stack).
- Integrate with **ELB** and **Auto Scaling**.

### Machine Learning & AI
- Train ML models using **GPU instances** (`p4`, `g5`).
- Use EC2 with **SageMaker**.

### Big Data & Analytics
- Run **Hadoop, Spark** clusters on EC2.
- Store data in **Amazon S3** and process with **EMR**.

### Gaming Servers
- Host multiplayer game servers with **low-latency connections**.

### High-Performance Computing (HPC)
- Scientific computing and simulations using **HPC6id** or **Nitro-based instances**.

---

## Best Practices for EC2
### Security Best Practices
- Use **IAM Roles** instead of storing credentials in the instance.
- Restrict **SSH/RDP access** using **Security Groups**.
- Enable **AWS GuardDuty** for anomaly detection.

### Cost Optimization
- Use **Spot Instances** for non-critical workloads.
- Right-size instances with **AWS Compute Optimizer**.
- Use **Reserved Instances** for long-term savings.

### Performance Optimization
- **Placement Groups** for low-latency networking.
- Enable **Enhanced Networking (ENA)** for high throughput.

