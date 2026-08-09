packets = ["normal", "hack attempt", "login","malware"]

for p in packets:

    if "hack" in p or "malware" in p:

        print("Intrusion Detected:", p)

    else:

        print("Normal:", p)
