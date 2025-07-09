# Topics covered:
- lifecycle rules
- Requester pays
- s3 event notifications

## S3 lifecycle rules: 
- it makes sense to move objects between storage tiers based on access patterns, allowing for major savings 
- tranistions can be performed manually but s3 lifecycle rules allow for a automatic way to accomplish this. 
- rules can be applied bucket-wide, to certain prefixes, or for specific object tags
- Amazon s3 analytics is a helpful tool to track object access patterns and decide lifecycle policies.
- Transition rules: configure objects to transition to another storage class based on access pattern
- Expiration action: configure objects to expire/delete after some time period, allows you to delete versions

## Requester pays: 
- In typical aws s3 pricing model the bucket owner pays for the storage costs as well as the networking costs
- Requester pays allows users to offload the networking cost onto the requestor of the object/data. 
- useful when you have large objects that require significant amounts networking costs. 
- typically used for sharing datasets with other accounts 
- for requester pays, the user must be authenticated with AWS(aws account), so that charges can be levied on them.

## S3 event notifications
- events are creation/deletion of objects, replication of objects and so on. 
- events can be filtered to focus on relevant information. 
- useful for automatically reacting to certain events happening in amazon s3. 
- events can trigger SNS, SQS queues or even lambda functions.
- iam policies need to defined to allow s3 to access individual services. 
- Events are sent to event bridge and can be sent to over 18 services from there. 
- Event bridge allows for event notifications to be super useful. features: 
    - advanced filtering: eg. filter based on object size, type, name, metadata
    - multiple destionations: events can be chanelled to multiple destinations 
    - event bridge capabilities: allows for events to be archived, replayed, improved reliability. 

