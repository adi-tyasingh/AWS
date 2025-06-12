# Topics Covered: 
- EC2 configuration options
- Security Groups
- stateless and stateful access for EC2 instances
- connecting with key value pairs (pem file)
- Bootstrap Script
- Images
- EC2 instance types
- EC2 purchasing options

## EC2 configs:
- OS -> (Linux, Windows, etc)
- CPU -> number of cores
- RAM -> amount of ram
- Storage -> type of storage(refer day 40)
- Network Card -> Public IP and speed of connection
- Firewall rules: security groups
- Bootstrap Script


# Security Groups:
- Inbound rules (By default Deny)
- outbound rules (By default Allow)
- Stateful and stateless
- A security group can be used multiple times. 
- locked down to region and VPC 
- Regulate access to: 
  + access to ports
  + Authorised IPv4 and IPv6 ranges
  + control of inbound traffic 
  + control of outbound traffic


### **1. Stateful Traffic (Security Groups)**
- **Definition**: A stateful firewall keeps track of the state of active connections. It automatically allows return traffic for an allowed request, even if there is no explicit rule for it.
- **Example**: AWS **Security Groups** are stateful.
- **How it Works**:
  - If an inbound rule allows traffic (e.g., SSH on port 22), the corresponding outbound response traffic is automatically allowed.
  - If an outbound rule allows traffic (e.g., HTTP request to a website), the inbound response is automatically allowed.
  - You **do not need to manually define return rules**.

### **2. Stateless Traffic (Network ACLs)**
- **Definition**: A stateless firewall does **not** track active connections. Every request and response must be explicitly allowed by separate inbound and outbound rules.
- **Example**: AWS **Network ACLs (NACLs)** are stateless.
- **How it Works**:
  - If you allow inbound traffic on port 80, you must also allow outbound traffic for return responses.
  - If you allow outbound traffic on port 443, you must also allow inbound responses.
  - Each direction (inbound and outbound) requires **explicit rules**.

### **Comparison Table**
| Feature         | Stateful (Security Groups) | Stateless (Network ACLs) |
|---------------|-----------------|----------------|
| Tracks connections? | ✅ Yes | ❌ No |
| Automatic response traffic? | ✅ Yes | ❌ No |
| Rules applied to? | Instance level | Subnet level |
| Example | Allow SSH (22) inbound → Response traffic auto-allowed | Allow SSH (22) inbound → Must manually allow outbound traffic |

### **Use Case**
- **Security Groups** (Stateful) are best for **controlling access at the instance level**.
- **Network ACLs** (Stateless) are best for **setting broader subnet-level security rules**, like blocking malicious IPs before they reach any instance.

### Important ports: 
- 22 : SSH & SFTP 
- 21 : FTP
- 80 : HTTP
- 443 : HTTPS 
- 3389 : RDS (windows instance connect)
--- 
# Connecting to an instance using Key value pair: 
**steps**: 
1. download pem file from aws console
2. Chmod the file (chmod 400)    `sudo chmod 400 key-file.pem`
3. run the following command:  `ssh -i 'key/file/path.pem' ec2-user@ec2-3-6-160-232.ap-south-1.compute.amazonaws.com`



# Bootstrap Script: 
- Allows us to provide a bash script that is run on the instance on startup. 
- Can be copy pasted / uploaded as a file. 
- ony executed once. 
- Executed on startup of the instance. 
- Usually contains commands for installation of certain software, running some software etc. 
- eg. running a docker container, installing nginx, etc. 

```bash 
sudo yum update -y
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
```

# AMI / Images : 
- you can create images from instances, this allows you to create a template, that can be reused in the future. 
- helpful when you need to create a lot of instances with the same software. 

### Steps to create an AMI:     
- select an instance 
- click on the actions option 
- select the create image option 

# EC2 instance Types: 
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
- eg. gpu accelerated 


# Purchasing options:

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


# Shared Responsibility Model for EC2: 
### Responsibilities of AWS: 
- Infrastructure (Global Network Security)
- Hardware maintainence
- Compliance Validation 
- Isolation on physical hosts

### User responsibilities: 
- Security group rules 
- Operating System patches and Updates 
- Software and utilities installed on the instance 
- IAM roles attached to instance 
- IAM access for users
- data security of the instance. 

# EC2 metadata: 
- Provides information about the running EC2 instance. 
- Can be accessed from inside the EC2 instance.  
- can be accessed via the metadata url: http://169.254.169.254/latest/meta-data/
- No authentication is needed since it is available inside an EC2 instance

