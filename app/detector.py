from app.rules import RULES

def detect_issues(metrics):
    issues = []

    for rule in RULES:
        if rule["condition"](metrics):
            issues.append({
                "issue": rule["name"],
                "severity": rule["severity"]
            })

    return issues
