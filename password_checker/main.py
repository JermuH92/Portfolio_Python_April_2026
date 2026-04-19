from rules import password_rules

def check_password(password, rules):
    
    return all(rule(password) for rule in rules) # All function returns True if every rule(password) rule is True

def get_failed_rules(password, rules):
	failed_rules = [rule.__name__ for rule in rules if not rule(password)]

	return failed_rules

test_password = "TestPassword123"
print(f"Checking password: {test_password}")

if check_password(test_password, password_rules):
	print(f"Is valid?: ✅ Password Accepted!")
else:
	failed = get_failed_rules(test_password, password_rules)
	print(f"❌ Password NOT Accepted. Failed Rules: {failed}")


    
