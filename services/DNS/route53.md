# Route 53
- Highly available, scalable and fully managed authoratative DNS service by AWS.
- All records can be edited by user 
- 100% availability SLA 
- Route 53 is also a domain registrar(allows you to buy a Domain)
- Hosted zones: container for records that define how to route traffic to a domain and it's subdomains
    - Public hosted zone: containes records that specify how to route traffic on the public internet 
    - Private hosted zone: records to route traffic within one or more VPCs. 
    - Hosted zones incur a charge of 50 cents per month per zone. 

![alt text](./assets/hosted-zones.png)

###  Alias:
- Allows hostname to be resolved to an **AWS resource** (eg: example.com -> load-balancer.amazonaws.com)
- Works for root (apex) domains and non-root domains (eg. root: example.com ; non-root: app.example.com)
- Free of charge
- Native health check capability
- Extension to DNS functionality 
- Does not allow user to set TTL 
- Automatically recognises IP changes to underlying resource 
- Alias records are always of type A/AAAA for AWS resource. 
- Only maps to an aws resource: 
    - ELB
    - Cloud Front 
    - API gateway 
    - Elastic beanstalk environments 
    - S3 websites 
    - VPC interface endpoints 
    - Global accelerator 
    - route 53 records in the same hosted zone
- Cannot set an alias for an Ec2 DNS name 

### Health checks: 
- HTTP health checks used to check underlying public resource health
- Useful for automated DNS failover 
- Health checks are integrated with cloud watch metrics. 
- Over 15 health checks all around the world, that all send requests to the resource. 
- users can set threshold, time interval, protocols for health checks.
- if >18% of checks pass route 53 considers the resource to be healthy
- health checks can also be set to pass or fail based on the first 5120 bytes of the text response
- resource should be configured to allow incoming health check requests 
- Types of health checks: 
    - checks that moniter an endpoint 
    - checks that moniter other health checks (calculated health checks)
    - Cloud watch health checks (full control, can be used to check private resource health)

### Routing policy: 
- Defines how route 53 responds to queries
- DNS does not actually route traffic(not in the way a load balancer does), DNS only answers queries 
- Types of policies: 
    - Simple: route traffic to a single resource, can specify multiple values, random value chosen if multiple values,  
    - Weighted:  Assign weights to specific values and direct traffic accordingly, useful for loadbalancing, testing new versions with small amount of traffic
    - Failover: primary and secondary resources, associated with health checks, if primary resource becomes unhealthy, traffic is routed to secondary
    - latency based: return ip to achieve minimal latency 
    - Geo-location: allows you to route traffic based on location on user within a specific continent, country or even state. Very useful for creating multiple versions of applications with diffrent languages, or diffrent countries having diffrent versions all together.  
    - multivalue answer: routes to multiple resources, can be associated with health checks, upto 8 healthy resources can be returned for a query.  
    - IP based: Define CIDR blocks and route users belonging to a certain block to a certain resource
    - geo-proximity: routes traffic based on location of user and location of DataCenter/resource(region for AWS resource and Coordinates for On-prem resources)
