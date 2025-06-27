# backups:
process and types of backups in RDS 

### Automated backups: 
- daily full backup of db conducted during backup window
- Transaction logs backed up every 5 mins 
- Allows for backup to any point in time starting from 5 mins ago. 
- Retention policy allows you to define the amount of time each backup is saved. 
- max retention = 35 days 
- min retentio  = 1 day 
- setting retention to 0 disables backups

### manual DB snapshots: 
- Triggered manually
- Indefinite retention 
- it is useful to snapshot db and restore to minimise storage costs(stopped dbs still incur storage costs)

### Aurora backups:
- automated backups, stored for 1 to 35 days 
- cannot disable backups
- point in time restore for 35 day period
- Manual snapshots are also possible, with indefinite retention. 

Note: restoring from snapshot creates a new db for aurora aswell as normal DBs 

### Restore from S3: 
- it is possible to restore mySql databases from a s3 bucket
- useful for migrating on-prem databases. 
- For normal mySQL create a snapshot of your db (onprem), upload to s3 and restore to rds MySQL. 
- For aurora MySQL, create a snapshot of onprem db using Percona Xtrabackup, upload to s3 and restore to RDS Aurora. 
