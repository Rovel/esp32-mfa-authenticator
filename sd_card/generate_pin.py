
import hmac
import hashlib
import secrets

def main():
    mode = input("Do you want to generate a 'pin' or a 'password'? ").strip().lower()
    if mode == "pin":
        pin = input("Enter your numeric PIN (6-20 digits): ")
        if not pin.isdigit() or not (6 <= len(pin) <= 20):
            print("Invalid PIN. Must be 6-20 digits.")
            return
        key = secrets.token_hex(16)
        digest = hmac.new(key.encode(), pin.encode(), hashlib.sha256).hexdigest()
    elif mode == "password":
        pwd = input("Enter your password (must have uppercase, digit, symbol, length > 8): ")
        # basic validation
        if (len(pwd) < 9 
            or pwd.islower() 
            or not any(ch.isdigit() for ch in pwd) 
            or pwd.isalnum()):
            print("Invalid password. Must have uppercase, digit, symbol, length > 8.")
            return
        key = secrets.token_hex(16)
        digest = hmac.new(key.encode(), pwd.encode(), hashlib.sha256).hexdigest()
    else:
        print("Invalid choice. Please choose 'pin' or 'password'.")
        return

    print(f"Your 32-char secret key: {key}")
    print(f"Your 64-char HMAC-SHA256 hash: {digest}")

if __name__ == "__main__":
    main()
