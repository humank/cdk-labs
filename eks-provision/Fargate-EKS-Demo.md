db: myeksdemo
us-west-2 regional ip group - pl-5aa44133


Create An AuroraDB from console, and copy domain name to add-rds-externalname.yml

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



aws eks --region us-west-2 update-kubeconfig --name myeks





add externalname to eks : 
kubectl apply -f add-rds-externalname.yml

add a amazonlinux server to visit aurora : 
kubectl apply -f shell-demo.yaml

connect into pod : 
kubectl exec -it shell-demo -- /bin/bash



Dig +search my-service

; <<>> DiG 9.9.4-RedHat-9.9.4-74.amzn2.1.2 <<>> +search my-service
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 985
;; flags: qr aa rd; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;my-service.default.svc.cluster.local. IN A

;; ANSWER SECTION:
my-service.default.svc.cluster.local. 5	IN CNAME myeksdemo-instance-1.cf6vkvlhpvat.us-west-2.rds.amazonaws.com.
myeksdemo-instance-1.cf6vkvlhpvat.us-west-2.rds.amazonaws.com. 5 IN A 192.168.91.233

-----

//create rds aurora for "myaurora"

vpc id = vpc-bb1ef4c3

subnet subnet-a7e0b2fd, subnet-e92e43a2

docker pull nginx

docker tag nginx:latest 584518143473.dkr.ecr.us-west-2.amazonaws.com/nginx:latest

$(aws ecr get-login --no-include-email)

docker push 584518143473.dkr.ecr.us-west-2.amazonaws.com/nginx:latest

//create lb
fargate lb create kim-alb2 --port HTTP:80 \
    --subnet-id subnet-a7e0b2fd \
    --subnet-id subnet-e92e43a2 \
    --security-group-id sg-c486e1b4 \
    --region us-west-2

fargate service create mynginx2 \
    --port HTTP:80 --lb kim-alb2 --num 3 \
    --image 584518143473.dkr.ecr.us-west-2.amazonaws.com/nginx:latest \
    --subnet-id subnet-a7e0b2fd \
    --subnet-id subnet-e92e43a2 \
    --security-group-id sg-c486e1b4 \
    --region us-west-2


fargate service destroy mynginx --region us-west-2