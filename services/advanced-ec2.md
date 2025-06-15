
## ✅ **1. Public, Private, and Elastic IP Addresses**

### 🔹 **Public IP Address**

* **Definition**: An IP assigned by AWS to an instance that allows it to communicate with the internet.
* **Characteristics**:

  * Assigned **automatically** from Amazon’s public IP pool.
  * **Ephemeral** – changes when:

    * You stop/start the instance.
    * The instance is terminated and recreated.
  * Used when the instance is in a public subnet and needs internet access via an **Internet Gateway**.
* **Use Case**: Temporary internet-facing instances like test servers.

---

### 🔹 **Private IP Address**

* **Definition**: An internal IP address used for communication within the VPC (Virtual Private Cloud).
* **Characteristics**:

  * Assigned automatically (or manually) from the CIDR block of your subnet.
  * **Persists** for the life of the instance (even after stop/start).
  * Cannot be used to connect to the internet unless **NAT Gateway** or **Internet Gateway** is used.
* **Use Case**: Backend services, internal APIs, database servers, etc.

---

### 🔹 **Elastic IP Address (EIP)**

* **Definition**: A **static**, **public IPv4** address you reserve in your AWS account.
* **Characteristics**:

  * You can associate and re-associate it with any instance.
  * You **own** it until you release it.
  * **Costs** are incurred **only** when:

    * The EIP is not associated with a running instance.
    * You have more than one EIP per region.
* **Use Case**: Stable public IP for services where consistency is required, e.g., DNS pointing, failover mechanisms.

---

### 🔄 Summary Table:

| Type       | Scope    | Lifetime                 | Use Case               | Charges           |
| ---------- | -------- | ------------------------ | ---------------------- | ----------------- |
| Public IP  | Public   | Temporary                | Internet-facing EC2    | Free (while used) |
| Private IP | Internal | Persistent               | Internal communication | Free              |
| Elastic IP | Public   | Static (user-controlled) | Stable public access   | May incur cost    |

---

## ✅ **2. Elastic Network Interfaces (ENIs)**

### 🔹 **What is an ENI?**

* A **virtual network interface card (vNIC)** in a VPC.
* Attached to EC2 instances to manage networking.
* Can be attached/detached from EC2 instances.

### 🔹 **Components of ENI**:

* Private IPs (primary and secondary)
* One or more security groups
* MAC address
* Elastic IP (optional)
* Public IP (optional)
* Source/destination check flag

### 🔹 **ENI Use Cases**:

1. **High Availability**: Move ENI from one instance to another in case of failure.
2. **Separate Traffic**: Use multiple ENIs for management, application, and monitoring traffic separation.
3. **Dual Network Interface**: Attach to multiple subnets (via multiple ENIs).

### 🔹 **ENI Types**:

| Type                        | Use Case                                        |
| --------------------------- | ----------------------------------------------- |
| Primary ENI                 | Attached at instance creation                   |
| Secondary ENI               | Manually attached/detached                      |
| Trunk ENI                   | Used with container-based workloads (e.g., ECS) |
| EF (Elastic Fabric Adapter) | High-performance computing                      |

---

## ✅ **3. Placement Groups**

### 🔹 **What is a Placement Group?**

* A logical grouping of EC2 instances that affects **placement strategy** for optimizing performance.

### 🔹 **Types of Placement Groups**:

| Type          | Description                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------------------- |
| **Cluster**   | Packs instances close together in one AZ – ideal for low-latency, high-throughput.                    |
| **Spread**    | Distributes instances across **different hardware** – reduces simultaneous failures.                  |
| **Partition** | Distributes instances across logical **partitions** within AZs – ideal for big data apps like Hadoop. |

### 🔹 **Use Cases**:

* **Cluster**: HPC, low-latency apps, tightly coupled workloads.
* **Spread**: Critical apps where instance isolation is key.
* **Partition**: Big data, distributed computing with fault isolation.

### 🔹 **Limits**:

* Spread Placement Group: Max **7 instances per AZ** (soft limit).
* Cluster: Must be in the **same AZ**.
* Partition: Max **7 partitions per AZ**, can span multiple AZs.

---

## ✅ **4. EC2 Hibernate**

### 🔹 **What is Hibernate?**

* A stop mechanism that **preserves in-memory RAM content**.
* On restart, the instance resumes **from where it left off**, like a laptop hibernate.

### 🔹 **How It Works**:

1. EC2 stores **RAM contents** on the root EBS volume (encrypted).
2. Instance is stopped (not terminated).
3. Upon start, AWS loads memory state back and resumes.

### 🔹 **Requirements**:

* Root volume must be **EBS (not instance store)**.
* EBS volume **must be encrypted**.
* Supported **instance types**: C3, C4, M3, M4, R3, R4, T2, T3, etc. (check region/instance support).
* **Max memory** supported for hibernation: **150 GB**.

### 🔹 **Pros**:

* Fast boot time (no OS cold start).
* Maintains application state.
* Useful for short-lived, interruption-prone workloads.

### 🔹 **Cons**:

* Longer stop/start cycle than traditional stop.
* Slightly higher cost (storage of RAM content on EBS).
* Limited to Linux and Windows only.

---

## 🧠 Final Notes

| Concept         | Key Purpose                              | Best Use Case                        |
| --------------- | ---------------------------------------- | ------------------------------------ |
| Public IP       | Internet access (ephemeral)              | Temporary or test servers            |
| Private IP      | Internal VPC communication               | Backend apps, databases              |
| Elastic IP      | Persistent public IP                     | Production servers, DNS-stable apps  |
| ENI             | Virtual NIC with customizable net config | HA setup, multiple network paths     |
| Placement Group | Optimize performance/fault tolerance     | HPC, big data, critical systems      |
| Hibernate       | Resume instance from memory snapshot     | Stateful services, reduced boot time |

