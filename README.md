# AWS Scalable Web Application

## Project Overview

A scalable containerized web application deployed on AWS using
Amazon ECS Fargate, Application Load Balancer, Amazon RDS,
Amazon ECR, AWS CloudFormation, CloudWatch and SNS.

## Architecture

[Architecture diagram]

## Technologies Used

- AWS ECS Fargate
- Amazon ECR
- Application Load Balancer
- Amazon RDS PostgreSQL
- Amazon VPC
- AWS CloudFormation
- Amazon CloudWatch
- Amazon SNS
- AWS Application Auto Scaling
- Docker
- Python
- Flask

## Application

The application exposes:

GET /

GET /health

## Infrastructure

The infrastructure is provisioned using AWS CloudFormation.

Template:

infrastructure/infrastructure.yaml

## Deployment

1. Build Docker image
2. Push image to Amazon ECR
3. Deploy CloudFormation stack
4. ECS Fargate launches the application
5. Application Load Balancer exposes the application
6. CloudWatch monitors the application

## Auto Scaling

Minimum tasks: 1
Maximum tasks: 3
CPU target: 60%

## Monitoring

CloudWatch monitors:

- ECS CPU utilization
- ECS memory utilization
- ECS running task count
- RDS CPU utilization
- RDS database connections
- ALB request count

CloudWatch alarms send notifications through SNS.

## Logging

ECS containers use the awslogs driver and send application
logs to CloudWatch Logs.

## Application Health Check

/health returns:

{"status":"healthy"}

## Deployment Output

Application URL:

<your ALB DNS URL>

## Submission

Screenshots and assignment documentation are available through
the OneDrive submission link.
