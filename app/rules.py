RULES = [
    {
        "name": "blocking",
        "condition": lambda m: any(x["wait_type"] == "LCK_M_X" for x in m),
        "severity": "HIGH"
    },
    {
        "name": "long_running_query",
        "condition": lambda m: any(x["wait_time"] > 5000 for x in m),
        "severity": "MEDIUM"
    },
    {
        "name": "cpu_pressure",
        "condition": lambda m: any(x.get("cpu_time", 0) > 10000 for x in m),
        "severity": "HIGH"
    }
]

