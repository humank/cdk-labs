#!/usr/bin/env python3

from aws_cdk import core
from ops.infra_stack import VpcStack
from ops.fargate_stack import FargateStack

environment = {'region': 'us-west-2'}
app = core.App()

myvpc = VpcStack(app, "VpcStack", env=environment)
vpcId = core.Fn.import_value("exportedId")


fargateCluster = FargateStack(vpcId,app, "FargateStack",environment=environment)


core.Tag.add(myvpc,'Name','demo')
app.synth()
