#!/usr/bin/env python3
from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elbv2,
    core,
)



class VpcStack(core.Stack):
      def __init__(self, app: core.App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        vpc = ec2.Vpc(
            self, 
            "Opsvpc",
            max_azs=3
        )

        asg = autoscaling.AutoScalingGroup(
            self,
            "ASG",
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.AmazonLinuxImage(),
        )

        lb = elbv2.ApplicationLoadBalancer(
            self, "OpsLB",
            vpc=vpc,
            internet_facing=True
        )

        listener = lb.add_listener("Listener", port=80)
        listener.add_targets("Target", port=80, targets=[asg])
        listener.connections.allow_default_port_from_any_ipv4("Open to the world")

        asg.scale_on_request_count("AModestLoad", target_requests_per_second=1)

        # Publish the custom resource output
        core.CfnOutput(
            self, "exportedId",
            description="The message that came back from the created stack",
            value=vpc.vpc_id,
        )

        