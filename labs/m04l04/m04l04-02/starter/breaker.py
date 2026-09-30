events = [False, False, False, True, True, True, False]
state, failures, probe = "closed", 0, False
for ok in events:
    if state == "open":
        print("fast fail")
        continue
    if state == "half" and probe:
        print("probe", "pass" if ok else "fail")
        state = "closed" if ok else "open"
        probe = False
        continue
    print("call", "ok" if ok else "error")
    failures = 0 if ok else failures + 1
    if failures == 3: state, probe = "open", False
