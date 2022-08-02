# wordpress-k8s-multi-tenancy
This is a sample project to demo how to run a enterprise grade app as multi-tenant solution in kubernetes

The issue is we are solving is that Kubernetes doesn't support multi-tenancy out of the box, however we want to have a solution for multi-tenancy setup for our SaaS application in Kubernetes.
Also, multi-tenancy in the context of our problem statement refers to deploying the same application for multiple customers in the same kubernetes cluster. So our customer would just have access to the SaaS application, without the need to access the kubernetes cluster itself.

Now the basic essence of multi-tenancy is to have isolation between the resources for different customers in a single kubernetes cluster. We can achieve this isolation at two level:
1. Control Plane level  and  2. Data plane Level.

Below are the list of isolations that we can implement in our kubernetes cluster at both of these levels.
1. Namespace Isolation: Namespace would help us to segregate multiple tenant's workload in a logical unit in a single cluster. This will allow us to implement different security policies, network policies, RBAC, etc for each of the tenants without affecting other tenants.
2. Resource Quota: This will help us to restrict the resource usage for each of the tenants, so that a single tenant should not be able to consume the majority of the cluster resources, thus avoiding the issue of "noisy-neighbour" in our cluster.
3. Network Isolation: This will help us to restrict the resource of one tenant to communicate with the resources of another tenant.
4. Storage Isolation: This will help us to segregate the data for each customer (tenant). Also, having seperate storage for each customer will help us set up different backup and restoration policies for each customer.
5. Restrict DNS Lookup: This will prevent the tenant in one namespace to lookup for service in another namespace, thus adding more layers of isolation.

Now all the above steps should be able to help us setup a solid multi-tenancy cluster for our customer.
In demo this, I plan to create a multi-tenant environment using minikube in my local computer and then deploy multiple instances of wordpress for each of these tenants.
