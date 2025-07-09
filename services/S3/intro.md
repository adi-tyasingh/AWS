# Simple Storage Service
- Higly available and durable object storage service
- Used by a very large number of websites
- Infinitely scalable 
- backbone service in AWS, integrates with a number of other service
- Use cases:
    - backup 
    - storage 
    - archives 
    - disaster recovery 
    - hybrid storage 
    - media storage 
    - application hosting 
    - data lakes and big data analytics 
    - static website hosting

### Buckets: 
- files are stored in buckets, works as a top level directory, all files in a bucket are called objects 
- bucket name must be globally unique 
    - names must be lowercase 
    - length should be between 3-63 charecters
    - cannot contain underscores 
    - cannot be ip 
    - cannot start with prefix 'xn--'
    - cannot end with suffix '-s3alias'
- buckets are defined in a specific region 
- each object has a key and value. 
- key is the full path name of the file, it can include '/' but it is not actually organised in folders. 
- value for each object is the actual data
- maximum object size: 5TB 
- For objects larger than 5GB, we need to use multipart uploads
- objects can have associated metadata and version ID 
- Versioning is a feature of S3 that allows for safe changes and prevents accidental deletions. 
    - stores version ID for all objects 
    - if versioning is turned on after bucket creation, pre-existing objects get a null version 
    - deletion just creates a deletion marker (soft delete)
    - suspending versioning does not delete already created versions 
- Replication: AWS allows you to replicate the contents of your bucket for redundancy and latency reasons 
    - Two types of replication: CRR(Cross region replication) & SRR(same region replication)
    - Buckets must have versioning enabled
    - Replication is asynchronous 
    - objects added after enabling replication are replicated, must use batch to replicate pre-existing objects 
    - No chaining of replication. 

### Security: 
- S3 has a number of features to ensure security.
- IAM policies: defines which IAM users can make which API calls
- Bucket Policies: bucket wide rules from the s3 console, allows cross account access
- Object ACL: fine grained object level access control (can be disabled)
- Bucket ACL: uncommon (can be disabled)
- Encryption policy: define if you want objects to be encrypted. enabled by default
- S3 buckets are by default configured to block all public access, to prevent data leaks
- You can configure you account to block all public access for all buckets. 

### Storage classes: 
- Standard 
- Infrequent access 
- One zone - infrequent access 
- Glacier Instant retrieval
- Glacier Flexible retrieval 
- Glacier Deep Archive 
- Intelligent tiering 