# Relational database service
Database serivce for database engines that use SQL as a query language, fully managed by AWS 

### Advantages:
- Managed service 
- AWS handles resource provisioning 
- OS Patches 
- Continous backups 
- Point in time backups 
- Monitering dashboards
- MultiAZ 
- read replicas 
- Manitanence windows 
- EBS storage 
- Vertical and horizontal scaling capability
- Storage Autoscaling
    - automatically increase storage capacity as needed 
    - Useful for applications with unpredicatable workloads 
    - supported for all db engines 
    - have to set a maximum threshold

### Supported engines: 
- Potgres 
- MySQL 
- MariaDB
- Oracle 
- Microsoft SQL server 
- IBM DB2 
- Aurora(Proprietary)

### RDS custom:
- for Oracle and Microsoft SQL server 
- Allows SSH and SSM access to underlying EC2 instance 
- Allows for full admin access 
- Allows for manual patching and configuration 
- Recommended to take a snapshot before trying customization 
- Disable automation mode

