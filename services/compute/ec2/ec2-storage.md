# EC2 Storage options: 

### EBS(Elastic Block Storage):
- Network volumes
- Locked to a specific AZ
- Allows instances to persist data even after termination 
- Can only be mounted to one instance at a time. 
- 30Gb in AWS free tier
- Latency due to network 
- detachable and can be attached to new instances. 
- capacity needs to specified along with IOPS
- Billed according to provisioned capacity. (Size and IOPS can be changed as needed)
- unattached ebs volumes are possible
- Delete on termination attribute. 
- Used as root volume for EC2 instances (By default root volumes are deleted on termination of instance)
- EBS Snapshots:
    - backup of EBS volume 
    - can be created without stopping instance 
    - stopping instance is recomended
    - can be transferred across AZs 
    - can be archived(75% cheaper)(retrieval time ~24h) 
    - EBS snapshot recyclebin 
    - Fast Snapshot restore


### AMI(Amazon machine Image):
- customization of an ec2 instance(pre-packaged) 
- add your own software, config, os, monitering .... 
- faster boot/config times because of pre-packaging. 
- region specific 
- Public AMIs (provided by AWS) eg. Amazon linux 2 
- Make your own AMI (from am EC2 instance)
- AWS marketplace also contains AMIs for sale
- AMI creation flow: 
    - start instance 
    - configure instance 
    - stop instance (for data integrity)
    - build an AMI (creates a snapshot in the bg)
- Instances can be launched using the created AMI 

### Instance Store:
- hardware disk attached directly to the machine
- Better IO performance
- Disk directly attached to instance (Not network volume)
- Ephemeral storage(deleted when instance is stopped)
- use cases: buffering, scratch data, temporary content. 