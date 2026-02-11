import requests
import json

# Test the authentication endpoints
BASE_URL = "http://localhost:8000"

def test_register():
    print("Testing registration endpoint...")
    register_url = f"{BASE_URL}/api/auth/register"

    # Test data
    user_data = {
        "email": "test@example.com",
        "password": "password123"
    }

    try:
        response = requests.post(register_url, json=user_data)
        print(f"Register Response: {response.status_code}")
        print(f"Register Data: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Register Error: {str(e)}")
        return False

def test_login():
    print("\nTesting login endpoint...")
    login_url = f"{BASE_URL}/api/auth/login"

    # Test data
    login_data = {
        "email": "test@example.com",
        "password": "password123"
    }

    try:
        response = requests.post(login_url, json=login_data)
        print(f"Login Response: {response.status_code}")
        print(f"Login Data: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Login Error: {str(e)}")
        return False

def test_verify():
    print("\nTesting verify endpoint...")
    verify_url = f"{BASE_URL}/api/auth/verify"

    # Use a dummy token for testing
    headers = {
        "Authorization": "Bearer dummy_token"
    }

    try:
        response = requests.get(verify_url, headers=headers)
        print(f"Verify Response: {response.status_code}")
        print(f"Verify Data: {response.json()}")
        return response.status_code in [200, 401]  # 401 is expected for invalid token
    except Exception as e:
        print(f"Verify Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing authentication endpoints...\n")

    # Test registration
    reg_success = test_register()

    # Test login
    login_success = test_login()

    # Test verify
    verify_success = test_verify()

    print(f"\nResults:")
    print(f"Register: {'PASS' if reg_success else 'FAIL'}")
    print(f"Login: {'PASS' if login_success else 'FAIL'}")
    print(f"Verify: {'PASS' if verify_success else 'FAIL'}")

    if all([reg_success, login_success, verify_success]):
        print("\nAll authentication endpoints are working!")
    else:
        print("\nSome endpoints may have issues.")