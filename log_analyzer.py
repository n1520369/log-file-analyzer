error_count = 0
warning_count = 0

with open("sample.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1

print(f"Errors Found: {error_count}")
print(f"Warnings Found: {warning_count}")
