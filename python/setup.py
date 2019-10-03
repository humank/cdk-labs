import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk-labs",
    version="0.0.1",

    description="A sample CDK Python app create VPC",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Kim Kao",

    package_dir={"": "ops"},
    packages=setuptools.find_packages(where="ops"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws_iam",
        "aws-cdk.aws_sqs",
        "aws-cdk.aws_sns",
        "aws-cdk.aws_sns_subscriptions",
        "aws-cdk.aws_s3",
        "aws-cdk.aws_ec2",
        "aws-cdk.aws-autoscaling",
        "aws_cdk.aws_elasticloadbalancingv2",
        "aws-cdk.aws_ecs",
        "aws-cdk.aws_ecs_patterns",
        "aws-cdk.aws_eks"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
