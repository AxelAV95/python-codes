from flask import Blueprint, request, jsonify, current_app
from src.database import db
from src.models.user import User
from src.schemas.user_schema import UserSchema, LoginSchema
import jwt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    schema = UserSchema()
    
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    if User.query.filter_by(email=validated_data['email']).first():
        return jsonify({'message': 'User already exists'}), 400
    
    user = User(
        email=validated_data['email'],
        password=validated_data['password']
    )
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    schema = LoginSchema()
    
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    user = User.query.filter_by(email=validated_data['email']).first()
    if not user or not user.check_password(validated_data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = jwt.encode(
        {'user_id': user.id},
        current_app.config['JWT_SECRET_KEY'],  # Usamos current_app en lugar de app
        algorithm='HS256'
    )
    
    return jsonify({'token': token}), 200