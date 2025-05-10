# Topics Covered:
- AWS OUs 
- AWS Control Tower
- AWS RAM
- AWS Service catalog 
- AWS pricing models
- Pricing calculator 
- AWS Compute optimiser 
- Cost and usage reports 
- Billing alarms
- AWS budget 
- AWS cost anomaly 
- AWS service quotas
- AWS trusted advisor


# Control Tower: 
- Automates setup of AWS organizations, governance policies and security baselines to provide a WA landing zone

# RAM(Resource access manager)
- Share resources between accounts and within your account
- with any account or within your organization 
- avoid resource duplication 
- supported resources: Aurora, VPC Subnets, Transit gateway, EC2 dedicated hosts


# Service Catalog:
**AWS Service Catalog** is a managed service that helps organizations centrally manage, deploy, and govern approved IT services and resources on AWS. It allows administrators to define and manage catalogs of pre-approved AWS resources, ensuring compliance, security, and cost control while giving users self-service access to provision resources.

---

## **Key Features**  

### 🔹 **Centralized IT Management**  
- Allows administrators to create, manage, and share catalogs of approved AWS services, such as EC2, RDS, and Lambda.  
- Enforces security, compliance, and governance policies.

### 🔹 **Self-Service Access**  
- Users can browse and provision pre-approved AWS resources through a user-friendly interface.  
- Reduces dependency on IT teams for resource provisioning.

### 🔹 **Standardized Deployment**  
- Uses AWS CloudFormation templates to enforce infrastructure as code (IaC).  
- Ensures consistency across deployed resources.

### 🔹 **Access Control & Governance**  
- Integrates with **AWS Identity and Access Management (IAM)** to control user permissions.  
- Limits what resources users can launch and configure.

### 🔹 **Cost Control & Tracking**  
- Helps organizations enforce budget constraints.  
- Tracks resource usage with AWS Cost Management tools.

---

## **Core Concepts**  

| Concept | Description |
|---------|------------|
| **Product** | A pre-configured AWS resource (e.g., EC2, RDS) defined in CloudFormation templates. |
| **Portfolio** | A collection of related products with defined access permissions. |
| **Constraints** | Rules that restrict how a product is deployed (e.g., instance types, regions). |
| **Launch Paths** | Configurations defining which IAM roles and constraints apply when launching a product. |
| **Provisioned Products** | Deployed instances of a product within a user's AWS account. |

---

## **Common Use Cases**  

✅ **IT Service Catalogs** – Organizations can offer a self-service catalog of IT-approved AWS resources.  
✅ **Compliance Enforcement** – Enforce security policies, tagging standards, and approved configurations.  
✅ **Cost Optimization** – Restrict services to only approved instance types and regions.  
✅ **Multi-Account Deployments** – Standardize resource deployment across multiple AWS accounts using AWS Organizations.  

---

## **Integration with Other AWS Services**  

- **AWS Organizations** – Share portfolios across multiple accounts.
- **AWS CloudFormation** – Define infrastructure as code.
- **AWS IAM** – Control user access and permissions.
- **AWS Budgets** – Set cost constraints for products.
- **AWS Lambda & AWS Step Functions** – Automate workflows for resource provisioning.

---

### 🚀 **Getting Started with AWS Service Catalog**  

1️⃣ **Create a Portfolio** – Define a collection of AWS services to offer.  
2️⃣ **Add Products** – Create AWS CloudFormation templates for approved resources.  
3️⃣ **Set Permissions** – Assign IAM roles and permissions for users.  
4️⃣ **Define Constraints** – Restrict resource configurations to ensure compliance.  
5️⃣ **Share the Portfolio** – Make the catalog available to users or multiple AWS accounts.  
6️⃣ **Users Provision Resources** – Users select and launch pre-approved services.  



# AWS pricing:
- EC2 pricing 
- S3 pricing
- Storage pricing 
- CDN - cloudfront pricing 
- Networking costs (charged / gb of transfer between regions, sometimes charged AZ to AZ as well) (private ip charges are less)
- Savings plans 
- Compute optimiser reviews: Ec2, Lambda, ASG, Ebs and gives recommendation after 14 days 

# AWS Pricing calculator: 
- Calculates montly costs based on expected usage

# Cost Anomaly detection 
- uses ml to identify anomalies in costs 
- detect anomalies in usage, users, taxes etc 

# AWS Trusted advisor: 
- no need for installation 
- high level service 