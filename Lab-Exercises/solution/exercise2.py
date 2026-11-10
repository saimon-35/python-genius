cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": [
        "10.0.1.15",
        "10.0.1.16",
        "10.0.1.17",
        "10.0.1.18",
        "10.0.1.19"
    ]
}


def calculate_capacity(config):

    # Step 1: Extract data from dictionary
    cluster_name = config["cluster_name"]
    total_slots = config["total_max_slots"]
    active_nodes = config["active_nodes"]

    # Step 2: Count active nodes using for loop
    active_count = 0

    for node in active_nodes:
        active_count += 1

    # Step 3: Calculate utilization percentage
    utilization = (active_count / total_slots) * 100

    # Step 4: Print summary report
    print("\n------ Cluster Audit Report ------")
    print(f"Cluster Name: {cluster_name}")
    print(f"Total Capacity: {total_slots}")
    print(f"Active Nodes: {active_count}")
    print(f"Cluster Utilization: {utilization}%")


# Execute the audit tool
calculate_capacity(cluster_config)