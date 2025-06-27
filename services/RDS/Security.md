# Security in RDS: 

### At-rest Encryption
- RDS databases can be encrypted using AWS KMS 
- If master is not encrypted, read-replicas cannot be encrypted 
- To encrypt an un-encrypted DB, snapshot and restore as encrypted
 

 ### In-fligh Encryption: 
 - RDS supports in-flight encryption by default 
 - use AWS TLS client certificates
 - IAM Authentication: IAM roles can be used to connect to DB instances(allowing EC2 and other serivices to access DB)
 - Security Groups: control network access 
 - No SSH access (Exception of RDS custom)
 - Audit logs can be enabled and saved long term in cloud watch
 