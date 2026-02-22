from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# DynamoDB connection (uses IAM role)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('UsersTable')


# CREATE
@app.route('/create', methods=['POST'])
def create_user():
    data = request.json
    table.put_item(Item=data)
    return jsonify({"message": "User created successfully"})


# READ
@app.route('/read/<user_id>', methods=['GET'])
def read_user(user_id):
    response = table.get_item(Key={'user_id': user_id})
    return jsonify(response.get('Item', {}))


# UPDATE
@app.route('/update/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    table.update_item(
        Key={'user_id': user_id},
        UpdateExpression="set #n = :name, age = :age",
        ExpressionAttributeNames={'#n': 'name'},
        ExpressionAttributeValues={
            ':name': data['name'],
            ':age': data['age']
        }
    )
    return jsonify({"message": "User updated successfully"})


# DELETE
@app.route('/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    table.delete_item(Key={'user_id': user_id})
    return jsonify({"message": "User deleted successfully"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)