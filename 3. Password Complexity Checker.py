import re

def password_strength(password):
    score = 0
    feedback = []
    
    # Length 
    if len(password) >= 12:
        score += 2
        feedback.append("✓ Length is good (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("✓ Length is acceptable (8+ characters)")
    else:
        feedback.append("⚠️ Password too short (less than 8 characters)")
    
    # Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("⚠️ No uppercase letters")
    
    # Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("⚠️ No lowercase letters")
    
    # Numbers
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("⚠️ No numbers")
    
    # Special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("⚠️ No special characters")
    
    # Strength feedback
    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, feedback

def main():
    print("\033[1;35mPassword Complexity Checker\033[0m")
    print("\033[0;36mEnter your password to check its strength:\033[0m")
    password = input("\033[0;32m> \033[0m")
    strength, feedback = password_strength(password)
    print("\n\033[1;33mResult:\033[0m")
    print(f"\033[0;34mStrength:\033[0m \033[1;37m{strength}\033[0m")
    print("\n\033[0;35mFeedback:\033[0m")
    for item in feedback:
        print(item)

if __name__ == "__main__":
    main()
