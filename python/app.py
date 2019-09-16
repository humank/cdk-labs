#!/usr/bin/env python3
import os
from aws_cdk import core
from aws_cdk.core import Stack, Construct, Environment
from ops.infra_stack import InfraStack
from ops.fargate_stack import FargateStack, CdkPyCrossStackFargateStack

app = core.App()

ACCOUNT = app.node.try_get_context('account') or os.environ.get(
    'CDK_DEFAULT_ACCOUNT', 'unknown')
REGION = app.node.try_get_context('region') or os.environ.get(
    'CDK_DEFAULT_REGION', 'unknown')

AWS_ENV = Environment(region=REGION, account=ACCOUNT)

baseStack = InfraStack(app, "VpcStack", env=AWS_ENV)

vpcId = core.Fn.import_value("exportedId")

# fargateCluster = FargateStack(app, "FargateStack",
#     vpcId=core.Token.as_list(core.Fn.import_value('ExportedVpcId'))[0],
#     env=AWS_ENV
# )

secFargate = CdkPyCrossStackFargateStack(app, "cdk-py-xstack-fargate-svc1",vpc=baseStack.vpc, env=AWS_ENV)
core.Tag.add(baseStack,'Name','demo')
app.synth()
