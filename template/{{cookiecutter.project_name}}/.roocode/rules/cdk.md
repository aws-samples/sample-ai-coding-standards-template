# AWS CDK Standards

## Resource Management

- Make all AWS resource changes through CDK code only
- Do not use AWS API directly to modify AWS services
- Do not name aws resource by yourself, let cdk generate those names. For example with DynamoDB or S3

## Deployment Process

- Deploy all changes using `cdk deploy` without approval
- All cdk commands are used through taskfile.dev
- Verify deployment success after each change
- Iterate and fix issues until deployment succeeds
