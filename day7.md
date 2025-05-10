# Topics Covered:
- VPC

Points:
- VPC & ELB are defined for a region 
- You can create 5 VPCs in a region
- You can create 200 Subnets in a VPC
- It is necessary to define gate ways and updating route tables to allow connections to be routed inside VPC 
- IGW: internet gateway, helps our vpc instances to connect with the internet. 
- Public subnets have a route to the internet gateway. 
- VPC Flow logs : capture information about IP traffic going to and from network interfaces in a VPC! They help with security analysis, network trouble shooting, and moniter traffic patterns.
- NAT (instance and gateways) 
- VPC peering! connect multiple AWS VPCs 
- if using VPC peering, IP address ranges need to distinct. 
- VPC endpoint: allows you to connect to AWS services using a private network instead of the public www network!
- Endpoints provide lower latency and enhanced security! 
- AWS private-link secure and scaleable method to connect a service to thousands of VPCs! 
- Site to site VPN: AWS VPC to on-prem data center
- Direct Connect: Establish a physical connection between On-prem DC and AWS, private secure and fast! 
- Elastic IP
