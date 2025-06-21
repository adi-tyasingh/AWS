# Auto Scaling groups: 
- Allows for automated scaling(creating/removal) of instances to match demand. 
- no of instances can be scaled out (increase active instances) or scaled in (decrease number of instances)
- ASG allows us to define a min and a max number of active instances
- ASG can be registered to a LB 
- Allows for creation of new instances automatically if instance is deemed unhealthy.
- To create an ASG you need to define a launch template. 
- Additionally you need to define: 
    - Min size 
    - Max size 
    - Scaling policies
- Scaling cool-downs: 
    - After a scaling event (in/out) the ASG will not create or remove instances for a period of time
    - This is known as the cooldown period(Allows metrics to stabalise)
    - Default value of 300s
- It is best to use ready-to-use AMIs to reduce configuration time, allowing requests to start getting served quickly(Faster stabalization of Metrics)

## Launch Template attributes:
- AMI
- Instance type 
- User data 
- EBS volumes 
- Security groups 
- SSH key pair 
- IAM roles for your EC2 instance 
- Network + Subnet info 
- Load balancer info 

## Scaling policies: 
- Possible to connect Cloudwatch alarms with ASG to automate scaling 
- An alarm moniters a metric such as RAM utilization, Network utilization or CPU utilization for all ASG instances
- Alarms can trigger scale out and scale in operations, which are defined using scale-out and sacle-in policies. 
- **Dynamic Scaling**: Type of scaling(easy to setup)
    - Target Tracking: Define a cloud watch metric and ideal value, ASG scales to keep values as close to ideal as possible (eg. average CPU utilization at 40%)
    - simple/step Scaling: Define a cloud watch metric and the value at which to scale. (eg. increase intance count at CPU utilization at 80%)
- **Scheduled Scaling**: If demand spikes at predictable time periods, scheduled scaling allows us to define a time and the number of instances to create. 
- **Predictive Scaling**: Continuously forecast load and schedule scaling ahead of time. Useful when historical load data is available

### Scaling Metrics(Good ones):
- Average CPU utilization across instances
- Request count per target. (Use if you know the ideal number of requests that one instance of your application can handle )
- Average Network in/out: useful for upload download (activities requiring siginificant amount of networking)

