## Steps for Pod accessing external services

* Create An AuroraDB from console, and copy domain name to add-rds-externalname.yml

* Create EKS cluster by eksctl, will automatically create node group

```
Create an EKS cluster : 
eksctl create cluster \
--name prod \
--version 1.14 \
--nodegroup-name standard-workers \
--node-type t3.medium \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4 \
--node-ami auto

```

* Set kubectl config to conneect to EKS control plane

```
aws eks --region us-west-2 update-kubeconfig --name myeks
```


* Add external to eks, update the add-rds-externalname.yml file for the created RDS endpoint. Then apply it.

```
kubectl apply -f add-rds-externalname.yml
```

* Deploy a sever pod to check the communication between pod and exterl service

```
kubectl apply -f shell-demo.yaml
```


* Connect into pod

```
kubectl exec -it shell-demo -- /bin/bash
```

* install essential tools for you to check network status, such as dig, host, nslookup ..etc, then check for the named service is knowable or not

```
Dig +search my-service
```
-----
## Tips to create ECS fargate by using fargatecli

At first, you need to download and build it. 
```
git clone https://github.com/awslabs/fargatecli
```

Pre-request: Have a golang 1.13 on build machine, and run 

```
Make build
```

Create a VPC or using exist VPC to provision ECS fargate cluster.

```

//create lb
fargate lb create your-alb --port HTTP:80 \
    --subnet-id subnet-axxxxx \
    --subnet-id subnet-exxxxx \
    --security-group-id sg-cxxxxx \
    --region us-west-2

fargate service create mynginx \
    --port HTTP:80 --lb your-alb --num 3 \
    --image ${aws-account-id}.dkr.ecr.us-west-2.amazonaws.com/nginx:latest \
    --subnet-id subnet-axxxxx \
    --subnet-id subnet-exxxxx \
    --security-group-id sg-xxxxx \
    --region us-west-2
    
//destroy service
fargate service destroy mynginx --region us-west-2
```

## Push a local image to ECR

```
docker pull nginx

docker tag nginx:latest {AWS-Account-id}.dkr.ecr.us-west-2.amazonaws.com/nginx:latest

$(aws ecr get-login --no-include-email)

docker push {AWS-Account-id}.dkr.ecr.us-west-2.amazonaws.com/nginx:latest

```
