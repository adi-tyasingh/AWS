# Topics covered:
- Why make a global application
- CDN
- VPC connections 
- Elastic IP 


# Global applications:
Advantages: 
- High availability 
- global reach: 
- Decreased Latency: faster delivery of packets 
- Disaster recovery: in case of Disaster in a particular region it is a good idea to have your application running in multiple AZs and Regions
- Attack protection: protection from DDos attacks


# CDN:
### **Why Do We Need CDNs?**  
A **Content Delivery Network (CDN)** is a network of distributed servers designed to deliver content (such as images, videos, scripts, stylesheets, and HTML pages) efficiently to users. The primary reasons for using a CDN are:

1. **Reduced Latency**: CDNs cache content in multiple geographical locations, reducing the time it takes for users to access data.
2. **Improved Load Times**: By serving content from the nearest edge server, a CDN speeds up website performance.
3. **Bandwidth Optimization**: CDNs reduce the load on origin servers by caching static content.
4. **DDoS Protection**: Many CDNs provide security features such as DDoS mitigation and Web Application Firewalls (WAF).
5. **Scalability**: They handle high traffic loads efficiently, preventing server overload.
6. **Reliability**: CDNs improve uptime by distributing traffic across multiple servers.

---

### **How AWS CloudFront Works**
AWS **CloudFront** is Amazon’s CDN service that securely delivers content with low latency and high transfer speeds. Here’s how it works:

1. **User Request**:  
   - A user requests content (e.g., a webpage, video, or image) through their browser.
   
2. **Nearest Edge Location Check**:  
   - CloudFront determines the nearest **Edge Location** (one of AWS’s globally distributed caching servers) to the user.
   
3. **Cache Hit or Miss**:  
   - If the content is **cached** in the edge location, it is served directly from there (**cache hit**).
   - If not, CloudFront retrieves the content from the **origin server** (e.g., an S3 bucket, EC2 instance, or an external server), caches it, and then serves it to the user (**cache miss**).

4. **Content Delivery**:  
   - The content is delivered to the user with minimal delay. Future requests for the same content are served from the cache, improving performance.

5. **TTL and Cache Expiry**:  
   - CloudFront follows caching rules set by the origin, such as **Time-to-Live (TTL)**, to decide when to refresh content.

---

### **Key Features of AWS CloudFront**
- **Edge Locations**: Over 400+ globally distributed caching servers.
- **Multiple Origins**: Supports AWS S3, EC2, and custom origins.
- **Security**: Integrates with AWS Shield, WAF, and IAM for access control.
- **Logging & Analytics**: Monitors performance and user activity.
- **Custom Rules**: Allows URL-based caching, redirects, and compression.


# VPC connections:
### **VPC Connection Options in AWS**  
An **Amazon Virtual Private Cloud (VPC)** lets you create a logically isolated network within AWS where you can launch resources like EC2 instances, databases, and containers. AWS provides several connection options to link a VPC with other networks, such as the internet, other AWS VPCs, or on-premises data centers.  

---

## **1. Internet Connectivity Options**  
If you need your VPC to communicate with the internet, you can use:  

### **a) Internet Gateway (IGW)**
   - Enables outbound and inbound internet access for public resources in a VPC.
   - Used for public-facing EC2 instances or web applications.
   - Must be attached to the VPC, and routes must be configured in the route table.
   - **Use Case:** Web servers, public APIs, and internet-facing applications.

### **b) NAT Gateway / NAT Instance**
   - Enables private instances to access the internet while keeping them non-public.
   - Used when you want outgoing internet access without exposing the instance publicly.
   - **Use Case:** Database servers, backend applications that need software updates.

---

## **2. VPC-to-VPC Connectivity**  
To connect multiple VPCs within AWS:  

### **a) VPC Peering**
   - Direct connection between two VPCs using AWS’s internal network.
   - Works across different AWS regions but does not support transitive peering.
   - **Use Case:** Communication between different environments (e.g., Dev & Prod VPCs).

### **b) AWS Transit Gateway**
   - Centralized hub for connecting multiple VPCs and on-premises networks.
   - Supports transitive routing, meaning VPCs can communicate indirectly through the Transit Gateway.
   - **Use Case:** Large-scale network architectures with multiple VPCs.

---

## **3. On-Premises Connectivity Options**  
For connecting AWS with an on-premises data center or corporate network:  

### **a) AWS Site-to-Site VPN**
   - Creates an encrypted tunnel between an on-premises network and AWS.
   - Uses IPsec for security.
   - **Use Case:** Secure communication between AWS and corporate networks.

### **b) AWS Direct Connect**
   - Dedicated physical network link between on-premises and AWS.
   - Provides higher bandwidth, lower latency, and more reliability than VPN.
   - **Use Case:** Large-scale data transfers, hybrid cloud setups.

### **c) AWS Transit Gateway with VPN or Direct Connect**
   - Allows multiple on-premises networks to connect to AWS via a single Transit Gateway.
   - **Use Case:** Enterprises with multiple branch offices or hybrid architectures.

---

## **4. Private Connectivity to AWS Services**  
If you need to access AWS services privately (without internet access):  

### **a) VPC Endpoints**
   - Allows secure access to AWS services (e.g., S3, DynamoDB) from within a VPC.
   - **Two Types:**
     - **Interface Endpoint:** Uses AWS PrivateLink (for services like AWS Lambda, API Gateway).
     - **Gateway Endpoint:** Used for S3 and DynamoDB.
   - **Use Case:** Secure cloud-native applications.

### **b) AWS PrivateLink**
   - Enables private communication between VPCs and AWS services (or third-party SaaS services).
   - **Use Case:** Connecting SaaS providers to customer VPCs securely.

---

### **Summary Table: VPC Connection Options**
| Connection Type          | Purpose | Works With | Use Case |
|--------------------------|---------|-----------|----------|
| **Internet Gateway** | Internet access | Public subnets | Web servers, public APIs |
| **NAT Gateway** | Private outbound internet | Private subnets | Backend servers, updates |
| **VPC Peering** | VPC-to-VPC connection | 2 VPCs | Direct VPC communication |
| **Transit Gateway** | Centralized VPC connection | Multiple VPCs | Large network architectures |
| **Site-to-Site VPN** | Encrypted AWS-to-on-premises | On-prem networks | Hybrid cloud, secure access |
| **Direct Connect** | Dedicated AWS-to-on-prem | Data centers | High-speed, low-latency access |
| **VPC Endpoints** | Private AWS service access | AWS services (S3, DynamoDB) | Serverless apps, security |
| **PrivateLink** | Private SaaS/AWS service access | VPCs & SaaS | Secure third-party services |


# Elastic IP: 

### **What is an AWS Elastic IP (EIP)?**  
An **Elastic IP (EIP)** is a **static, public IPv4 address** provided by AWS that you can assign to EC2 instances, NAT Gateways, or other AWS resources. Unlike dynamic public IPs, an EIP remains associated with your AWS account until you explicitly release it.

---

## **Why Use Elastic IPs?**  
1. **Static Public IP Address**  
   - Regular public IPs assigned to EC2 instances change when the instance is stopped and restarted.
   - EIPs ensure that a resource maintains the same IP address over time.

2. **High Availability & Failover**  
   - If an instance fails, you can quickly remap the EIP to another instance to ensure minimal downtime.

3. **Control Over IP Addressing**  
   - You can reassign an EIP from one EC2 instance to another without needing DNS updates.

---

## **How AWS Elastic IPs Work**
1. **Allocate an EIP**  
   - You first allocate an Elastic IP from AWS’s public pool.
   - The IP belongs to your AWS account until you release it.

2. **Associate the EIP**  
   - You can associate an EIP with an **EC2 instance**, a **NAT Gateway**, or a **network interface**.

3. **Reassignment and Failover**  
   - If an EC2 instance fails, you can quickly move the EIP to a new instance to ensure continuity.

4. **Release the EIP**  
   - If you no longer need an EIP, you must disassociate it from any resource and release it back to AWS.

---

## **Key Considerations**
- **Costs**:  
  - **EIPs are free** when associated with a running instance.
  - **You are charged** if an EIP is allocated but not in use.
  
- **EIP Limits**:  
  - By default, you can have **5 EIPs per AWS account per region** (can request an increase).

- **IPv6 Support**:  
  - EIPs only work with **IPv4**. AWS does not provide Elastic IPs for IPv6.

---

## **Use Cases**
✅ Hosting applications that need a fixed IP for external access.  
✅ Setting up failover strategies to minimize downtime.  
✅ Assigning a known IP for whitelisting in security groups and firewalls.  
