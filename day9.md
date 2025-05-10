# topics covered:
- Cloud Formation: 
- Cloud Development kit 
- Web app 3-tier architecture 
- Global Accelerator 
- Elastic Beanstalk 
- CodeDeploy
- CodeCommit


# cloud Formation:
- Infrastructure as a Code
- used to deploy and manage services at scale
- Part of Operational Excellence
- Declarative method to specify resources 
- Can be declared using a YAML file 
- Declarative Templates: Define resources like EC2, S3, RDS, Lambda, IAM roles, etc.
- Stack Management: A stack is a collection of resources managed as a unit.
- Stacks can be managed, and deleted as a unit. 
- it is possible to track costs for a stack.
- Can be created using a GUI 

## Benefits of AWS CF:
- IAC : no need for manually allocating resources 
- Cost: 


```YAML 
AWSTemplateFormatVersion: "2010-09-09"
Description: Example CloudFormation template
Resources:
  MyEC2Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      ImageId: "ami-0abcdef1234567890"
      InstanceType: "t2.micro"
      Tags:
        - Key: "Name"
          Value: "MyServer"

```



# AWS Cloud Development Kit: 
- tools provided by AWS to aide in development on the cloud. 

# Web app 3-tier:
- ELB 
- Instances 
- RDS
- Elasticache: Memory based storage

# Elastic Beanstalk:
- PaaS 
- Developer centric view of deploying an application on AWS 
- it uses Ec2, ASG, ELB, RDS 
- Automatically manages all of the infrastructure
- End to end web application management
- Beanstalk is free but you pay for instances 

# AWS codeDeploy
- Deployment automation service 
- EC2, Fargate, Lambda, On-prem
- Hybrid (On-prem, AWS)
- Automates Deployemnt 
- Supports multiple compute services 
- Zero Downtime 
- Rollback support 
- Scalability 
- Smooth rolling updates 

# codeCommit 
- discontinued 

# CodeBuild:
- code building in the cloud 
- complies sc, runs test, produces pkgs that are ready to be deployed 

# Code Artifact 
- 

# 