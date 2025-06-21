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
- EBS types:
    - gp2(legacy)/gp3: general purspose ssd volume (used most commonly, balance of price and performance)
    - io1/io2: highest performance SSD volume for mission critical (HT/LL) tasks
    - st1(throughput optimised): low cost HDD volume, throughput intensive, frequently accessed data. 
    - sc1(cold hdd): lowest cost HDD volume, for less frequently accessed data
- Provisioned IOPS(PIOPS):
    - critical applications that need a certain amount of IOPS(sustained IOPS performance)
    - Applications that need high IOPS(>16k)
    - great for DB workloads
    - io1: (4GiB - 16Tib) (IOPS: 64k for Nitro instances, 32k for normal instances)
    - io2(Block express): (4Gib - 64Tib) (IOPS: 256k)
    - Supports EBS multi-attach.
- HDD Usecases: 
    - cannot be boot volumes 
    - size: 125Gib - 16TiB
    - two kinds(st1 & sc1)
    - st1: big data processing, data warehouses, log processing (throughput: 500MiB) (IOPS: 500)
    - sc1: infrequently accessed data, low cost applications (Throughput: 250MiB) (IOPS: 250)
- Multi-attach:
    - allows for attaching a single EBS volume to multiple EC2 instances in the same availability zone. 
    - Only available for IO1 & IO2 volumes. 
    - each instance has full read write access to volume (both can read and write at the same time)
    - Use cases: high application availability, application must manage concurrent writes. 
    - can only attach a maximum of 16 instances to a volume. 
    - use a cluster aware file system(not xfs and ext4)
- Encryption: 
    - encrypts data at rest. 
    - encrypts data in transit from EC2 to ebs volume 
    - encrypts snapshots and volumes created from snapshots. 
    - encryption and decryption handled transparently 
    - minimal impact on latency 
    - uses KMS (aes-256)
    - encrypting a volume: unencrypted vol -> snapshot -> encrypt snapshot -> create vol from snapshot(encryted vol created)
NOTE:
- only gp and io volumes can be used as root volumes. 
- for gp2 iops and throughput are linked(max 16k iops, only possible with >5tb of storage)
- for gp3 iops and throughput can be adjusted independently(max 16k iops)


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
- risk of data loss in case of faliure! 
- customer responsibility to back up data! 

### Amazon EFS(Elastic File System):
- Managed NFS 
- can be mounted by many ec2 instances
- highly available, scalable, expensive(3 x gp2)
- no need to provision capacity in advance(pay per use)(No capacity planning)
- use cases: content management, web-serving, data sharing, wordpress
- Uses NFS protocol internally 
- need to setup security group to control access 
- only compatible with linux based AMIs(not windows)
- Encryption at rest using KMS 
- POSIX file system (standard filesystem API)
- scale: 1000s of concurrent NFS clients, 10+ GiB throughput, grow to petabyte scale
- Performance modes: 
    - General purpose: latency sensitive use-cases
    - Max-IO: higher latency, greater parralleization, higher throughput
    Throughput modes: bursting, Provisioned, Elastic
- EFS tiers: 
    - standard: for frequently accessed files 
    - EFS-IA(infrequent access): cost for retrieval & lower storage cost. 
    - Archive: for rarely accessed data, much cheaper 
- Life cycle policies can be defined to intelligently move files between tiers. 
- Availability & Durability: 
    - standard: great for prod workloads 
    - one zone: cheapers & less durable/available, good for dev/test workloads

