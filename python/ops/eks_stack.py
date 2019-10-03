from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    core,
    aws_eks as eks,
    
)


class EksStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = vpc



        cluster = ecs.Cluster(self, 'Cluster', vpc=self.vpc)
        svc = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, 'FargateService',
            cluster=cluster,
            image=ecs.ContainerImage.from_registry('nginx'))

        core.CfnOutput(self, 'ServiceURL', value='http://{}/'.format(svc.load_balancer.load_balancer_full_name))