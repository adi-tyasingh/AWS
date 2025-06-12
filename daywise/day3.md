
Important points:
- Buckets are organise files in a flat manner, Buckets do not have a directory system. 
- files upload override files with the same name
- bucket access is defined using IAM policies, bucket policies. 
- buckets can have versioning allowing you to store multiple verisons of a file! protecting from unintended deletions and changes to files. 
- Pricing and access speeds differ based on storage class, refer below for more information. 

### Pricing model:
- Storage used (Charged based on the amount of storage used in GB/TB)
- Transfer and retrieval (Bucket transfers within the same region is free)
- number of requests sent(GET, PUT, DELETE)

### Recommended access control: 
- emplyees should be able have read only access to buckets(list, view, etc)
- employees should not be able to delete contents from buckets. 
- you need to define policies with custon, allow and deny conditions to ensure this. 

### Data Redundancy: 
- Enable cross region replication to ensure that data is available even in the scenario where one Region goes down. 


### **Key Features of AWS S3 (Amazon Simple Storage Service)**  

AWS S3 is a highly scalable, secure, and durable object storage service. Here are its key features:  

### **1. Storage & Scalability**  
- **Virtually Unlimited Storage** – No predefined storage limit; scales automatically.  
- **Object-Based Storage** – Stores data as objects rather than files or blocks.  
- **Multi-Region Storage** – Offers options for storing data across multiple AWS regions for redundancy.  

### **2. Data Durability & Availability**  
- **11 Nines Durability (99.999999999%)** – Highly durable, with automatic replication across multiple Availability Zones.  
- **High Availability** – Designed for 99.99% availability in Standard storage class.  

### **3. Storage Classes** *(for cost optimization based on access patterns)*  
- **S3 Standard** – High durability, low latency, frequently accessed data.  
- **S3 Intelligent-Tiering** – Moves objects automatically between two tiers (frequent/infrequent access) to optimize costs.  
- **S3 Standard-IA (Infrequent Access)** – Cheaper storage, but retrieval costs apply.  
- **S3 One Zone-IA** – Lower cost but stored in a single AZ.  
- **S3 Glacier** – Low-cost, long-term archive storage, retrieval in minutes to hours.  
- **S3 Glacier Deep Archive** – Lowest-cost storage, retrieval takes hours.  

### **4. Security & Compliance**  
- **Encryption** – Supports Server-Side Encryption (SSE-S3, SSE-KMS, SSE-C) and Client-Side Encryption.  
- **Access Control** – IAM policies, Bucket Policies, ACLs, and Access Points for granular control.  
- **Data Protection** – Supports AWS Backup, Versioning, and Object Lock for ransomware protection.  
- **Compliance** – Meets various industry standards (HIPAA, GDPR, SOC, PCI-DSS, etc.).  

### **5. Performance & Data Transfer**  
- **High Throughput & Low Latency** – Supports parallel uploads/downloads for faster data transfer.  
- **S3 Transfer Acceleration** – Speeds up transfers using AWS Edge Locations (CloudFront).  
- **Multi-Part Upload** – Optimized for uploading large files in parts, improving performance.  
- **Amazon S3 Express One Zone** – Low-latency access for high-performance workloads.  

### **6. Data Management & Analytics**  
- **S3 Object Lifecycle Management** – Automates data movement between storage classes based on rules.  
- **S3 Replication** – Cross-Region Replication (CRR) and Same-Region Replication (SRR) for redundancy.  
- **S3 Storage Lens** – Provides insights into storage usage and access patterns.  
- **S3 Select & S3 Glacier Select** – Query and retrieve specific data from objects using SQL-like queries.  

### **7. Integration & Compute Features**  
- **AWS Lambda Integration** – Triggers Lambda functions when objects are created or modified.  
- **Event Notifications** – Supports SNS, SQS, and Lambda for event-driven workflows.  
- **AWS Athena** – Query data directly from S3 using SQL without a database.  
- **Data Lake Integration** – Used with AWS Glue, Lake Formation, and Redshift Spectrum for big data processing.  

### **8. Versioning & Data Protection**  
- **Versioning** – Keeps multiple versions of objects to prevent accidental deletion.  
- **Object Lock & WORM (Write Once Read Many)** – Prevents object modification for regulatory compliance.  
- **Replication Time Control (RTC)** – Ensures predictable replication times.  

### **9. Cost Optimization & Billing**  
- **Pay-As-You-Go Pricing** – Pay only for what you use.  
- **Intelligent-Tiering** – Automatically moves objects to lower-cost storage based on usage.  
- **Lifecycle Policies** – Automates data deletion or transitions to cheaper storage classes.  


### **AWS S3: Important Facts & Key Specifications**  

#### **1. Object Size & Storage Limits**  
- **Maximum Object Size**: 5 TB (but objects larger than 5 GB must use multipart upload).  
- **Minimum Object Size**: No minimum size, but small files may not be cost-efficient.  
- **Bucket Limits**:  
  - 100 buckets per AWS account by default (soft limit, can be increased).  
  - Unlimited objects per bucket.  

#### **2. Storage Semantics**  
- **S3 is Not a File System**:  
  - It is an **object storage** system, meaning it does not support file system features like true directories or file locking.  
  - Files (objects) are stored in a **flat namespace** using keys that simulate directory structures (e.g., `folder1/file.txt`).  
  - Unlike a traditional file system, updates replace the entire object (no partial modifications).  

#### **3. Storage Performance & Throughput**  
- **Read/Write Throughput**:  
  - High throughput with **up to thousands of requests per second per prefix**.  
  - Performance scales with **multiple prefixes** (`folder1/`, `folder2/` to distribute load).  
- **Latency**:  
  - Typically **low millisecond latency** for reads and writes.  
  - S3 Express One Zone offers even lower latency for performance-sensitive applications.  
- **Multi-Part Upload**:  
  - Required for objects **>5 GB**, recommended for **>100 MB**.  
  - Allows parallel uploads for better performance.  

#### **4. Strong Consistency Model**  
- **Strong Read-After-Write Consistency** for all operations:  
  - Any newly written or updated object is **immediately visible**.  
  - No eventual consistency issues.  

---

### **AWS S3 Directory Buckets (New Feature)**  
#### **1. What are Directory Buckets?**  
- **Introduced in re:Invent 2023**, Directory Buckets offer **file-system-like** behavior in S3.  
- Designed to **bridge the gap** between object storage and traditional file systems.  

#### **2. Key Differences from General-Purpose S3 Buckets**  
| Feature               | General-Purpose S3 Bucket | Directory Bucket |
|-----------------------|--------------------------|-----------------|
| **Storage Structure** | Flat namespace (object keys) | True hierarchical directories |
| **Access Protocols**  | S3 API                    | S3 API + File system APIs (NFS/SMB-like behavior) |
| **Consistency**       | Strong, per-object        | Strong, across directories |
| **Use Cases**         | Cloud storage, backups, data lakes | Analytics, big data, file system workloads |
| **Performance**       | Optimized for object storage | Optimized for hierarchical access |
| **Locks & File Operations** | No file locking, full object updates | Supports directory-aware operations |

#### **3. Key Benefits of Directory Buckets**  
- **Supports Directory Structures** – True hierarchical storage instead of key prefixes.  
- **Faster Access for File-Oriented Workloads** – Better suited for analytics and distributed workloads.  
- **More Natural Integration with File-Based Applications** – Works well for applications expecting directories.  




