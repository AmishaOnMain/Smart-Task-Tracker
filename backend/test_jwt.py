from app.auth.jwt import create_access_token, verify_access_token

token = create_access_token(5)

print("Generated Token:")
print(token)

print()

payload = verify_access_token(token)

print("Decoded Payload:")
print(payload)