# for windows users to run this code, open powershell and run the following commands
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# python -m venv venv
# venv\Scripts\activate
# pip install flask pyotp qrcode pillow

from flask import Flask, request, jsonify, send_file
import pyotp
import qrcode
import io

app = Flask(__name__)

# This should be stored securely for each user in a real application
user_secrets = {}

@app.route('/generate-2fa/<username>', methods=['GET'])
def generate_2fa(username):
    # Generate a new secret key for the user
    secret = pyotp.random_base32()
    user_secrets[username] = secret

    # Create provisioning URI for the user
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name=username, issuer_name='Data_Integrity_Section_2FA')

    # Generate QR code
    qr = qrcode.make(uri)
    img = io.BytesIO()
    qr.save(img)
    img.seek(0)

    return send_file(img, mimetype='image/png')

@app.route('/verify-2fa/<username>', methods=['POST'])
def verify_2fa(username):
    user_code = request.json.get('code')
    secret = user_secrets.get(username)

    if not secret:
        return jsonify({'message': 'User not found or 2FA not set up'}), 404

    totp = pyotp.TOTP(secret)
    if totp.verify(user_code):
        return jsonify({'message': '2FA verified successfully'})
    else:
        return jsonify({'message': 'Invalid or expired code'}), 401

if __name__ == '__main__':
    app.run(debug=True)
