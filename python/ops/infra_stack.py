#!/usr/bin/env python3
from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elbv2,
    core,
)

class InfraStack(core.Stack):
      def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(self, "Vpc",max_azs=3)

        # Publish the custom resource output
        core.CfnOutput(self, 'vpcId', value=self.vpc.vpc_id, export_name='ExportedVpcId')

        # asg = autoscaling.AutoScalingGroup(
        #     self,
        #     "ASG",
        #     vpc=vpc,
        #     instance_type=ec2.InstanceType.of(
        #         ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
        #     ),
        #     machine_image=ec2.AmazonLinuxImage(),
        # )

        # lb = elbv2.ApplicationLoadBalancer(
        #     self, "OpsLB",
        #     vpc=vpc,
        #     internet_facing=True
        # )

        # listener = lb.add_listener("Listener", port=80)
        # listener.add_targets("Target", port=80, targets=[asg])
        # listener.connections.allow_default_port_from_any_ipv4("Open to the world")

        # asg.scale_on_request_count("AModestLoad", target_requests_per_second=1)

        

        