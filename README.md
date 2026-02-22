# AWS Lab 5 – DynamoDB Deployment and EC2 Integration

## Overview

This project demonstrates deployment of **AWS DynamoDB** and integration with an **EC2-hosted application**.

The application performs all required **CRUD operations**:
- Create
- Read
- Update
- Delete

Region used: **us-east-1 (N. Virginia)**

No hardcoded AWS credentials are used. Access is provided securely via an **IAM Role attached to EC2**.

---

## Architecture

EC2 Instance → IAM Role → DynamoDB (UsersTable)

- EC2 hosts the Flask application.
- IAM Role grants DynamoDB access.
- DynamoDB stores user data.

---

## DynamoDB Table Configuration

**Service:** Amazon DynamoDB  
**Region:** us-east-1  
**Table Name:** UsersTable  
**Partition Key:** user_id (String)  
**Capacity Mode:** On-demand  

---

## IAM Role Configuration

1. Go to **IAM → Create Role**
2. Trusted Entity Type: **AWS Service**
3. Use Case: **EC2**
4. Attach Policy: `AmazonDynamoDBFullAccess`
5. Attach role to EC2 instance via:
   - EC2 → Actions → Security → Modify IAM Role

### Security Compliance

- No AWS Access Keys used in code
- Access granted only through IAM Role
- Follows AWS best security practices

---

## CRUD Operations Implementation

### Create
Uses `put_item()` to insert a new record into DynamoDB.

### Read
Uses `get_item()` to retrieve a record by `user_id`.

### Update
Uses `update_item()` to modify existing attributes.

### Delete
Uses `delete_item()` to remove a record from the table.

---

## Running the Application on EC2

### Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install flask boto3
