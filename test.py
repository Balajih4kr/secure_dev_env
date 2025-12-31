assigned_ips = ["10.0.0.3", "10.0.0.2"]


for j in range(1, 255):
    ips = f"10.0.0.{j}"
    
    if ips not in assigned_ips:
        print(ips)
        break       