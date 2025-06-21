# Read-replicas:
- Scale reads 
- upto 15 read replicas 
- Read replicas can be within the same AZ or multiAz 
- replication in ASYNC 
- replicas are eventually consistent 
- Replicas can be promoted to independent db 
- Application should use multiple connection strings to take advantage of all read replicas. 
- Only select operations can be performed on read-replicas(NO DELETE/UPDATE/Insert)
- networking costs: 
    - No cost for RDS traffic between AZs(within same region)
    - cost incurred for multi-region read replicas
- Demo usecase:
    - Main operational DB is already having high load 
    - Analytics team wants to perform some operations on the DB 
    - Read replicas can prevent new load from overwhelming op db 

# Multi-AZ
- Allows for sync replication of DB between multiple RDS DBS 
- Master DB accepts and handles requests
- Single DNS name 
- Increased Availability 
- Failover in case of loss of AZ, loss of network or storage failure 
- Not used for scaling 
- standy db cannot be used for reads and writes
- Single AZ RDS can be converted to multi AZ (Zero-downtime operation)


NOTE: multi-AZ read-replica can also be used to increase Availability and for diaster recovery 


