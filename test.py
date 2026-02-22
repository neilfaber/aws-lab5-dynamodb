import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('UsersTable')

# CREATE
table.put_item(
    Item={
        'user_id': '300',
        'name': 'Neil',
        'age': 22,
        'is_active': True
    }
)
print("Item inserted successfully")

# READ
response = table.get_item(Key={'user_id': '300'})
print("Read:", response['Item'])

# UPDATE
table.update_item(
    Key={'user_id': '300'},
    UpdateExpression="set age = :a",
    ExpressionAttributeValues={':a': 25}
)
print("Item updated successfully")

# DELETE
table.delete_item(Key={'user_id': '300'})
print("Item deleted successfully")