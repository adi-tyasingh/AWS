# Scalability: 
- ability to handle greater workloads
- ability of application to adjust to greater demand 
- kinds of scalability: vertical & horizontal
- Vertical 
    - increasing the size of an instance(processing/request handling capacity) 
    - eg: t2.micro -> t2.large
    - used with non-distrubuted systems
- Horizontal
    - increasing the number of instances & systems. 
    - eg. one t2.micro -> 5 t2.micro 
    - used with distributed systems


# Availability: 
- running your applications in a way to maximise application up-time
- ensure that application can survive DC loss, or even AZ loss.
- involves running your application in multiple DCs/AZs/Regions. 
- passive high availability: high availability system has been built by AWS. eg: RDS multi-AZ 
- Active high availability: High availability system needs to be built: eg. horizontal scaling, ASG, ELB
- Typically some forms of horizontal scaling lead to increased availability.
- horizontal scaling through multi-AZ ASG & Multi-AZ load balancers increase Availability. 
