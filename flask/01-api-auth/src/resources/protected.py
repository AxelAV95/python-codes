from flask import Blueprint, jsonify
from src.utils.auth_utils import token_required

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/public', methods=['GET'])
def public_endpoint():
    return jsonify({'message': 'This is a public endpoint'}), 200

@protected_bp.route('/protected', methods=['GET'])
@token_required
def protected_endpoint(current_user):
    return jsonify({
        'message': 'This is a protected endpoint',
        'user_email': current_user.email
    }), 200