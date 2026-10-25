"""Candidate implementation. Follow README.md; no solution is provided."""

def dispatch_level(severity, people):
    if not isinstance(severity, str):
        raise TypeError("Severity must be a string")
    if type(people) is not int:
        raise TypeError("value must be an integer")
    if severity not in ("low", "medium", "high"):
        raise ValueError("invallid severity")
    if people <= 0:
        raise ValueError("people must be positive")
    if severity == "high" and  people >= 10:
         return "critical"
    elif severity == "high" or people >= 10:
        return "high"
    elif severity == "medium" or people >= 3:
        return "medium"
    else:
        return "low"
