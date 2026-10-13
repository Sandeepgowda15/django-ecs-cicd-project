# Production-Ready Django Deployment on AWS ECS

## Project Overview

Automated CI/CD pipeline for deploying a containerized Django application on AWS ECS Fargate.

## Architecture

Developer → GitHub → AWS CodePipeline → AWS CodeBuild → Amazon ECR → Amazon ECS Fargate → Application Load Balancer → Django Application

## AWS Services

- AWS CodePipeline – CI/CD orchestration
- AWS CodeBuild – Docker image building
- Amazon ECR – Docker image registry
- Amazon ECS Fargate – Container deployment
- Application Load Balancer – Application traffic routing
- AWS IAM – Access management
- AWS Secrets Manager – Secure Django secret storage
- Amazon CloudWatch Logs – Application logs

## Application Endpoints

- Home: `/`
- Health check: `/health/`
- Django admin: `/admin/`

## CI/CD Workflow

1. Push changes to the GitHub `main` branch.
2. CodePipeline starts automatically.
3. CodeBuild builds the Docker image.
4. The image is pushed to Amazon ECR with a build-specific tag.
5. ECS deploys the new image.
6. The application is verified through the load balancer.

## Security

- Django secret key stored in AWS Secrets Manager.
- IAM roles used for AWS service access.
- Django debugging disabled in production.
- Local AWS configuration files excluded from Git.

## Deployment Verification

- Source stage: Succeeded
- Build stage: Succeeded
- Deploy stage: Succeeded
- ECS service reached a steady state.
- `/health/` returned HTTP 200.
- `/` returned HTTP 200.

## Future Improvements

- Add automated Django tests.
- Configure HTTPS using AWS Certificate Manager.
- Add CloudWatch alarms.
- Manage infrastructure with Terraform.
- Optimize AWS resource costs.
