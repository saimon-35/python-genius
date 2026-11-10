def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):

    # Step 1: Calculate total monthly cost
    total_cost = instance_count * hourly_rate * 720

    # Step 2: Check budget
    if total_cost > budget_cap:
        exceeded_amount = total_cost - budget_cap

        return f"REJECTED: Budget Exceeded by ${exceeded_amount:.2f}!"

    else:
        return f"APPROVED: Total Estimated Cost is ${total_cost:.2f}."


# Test Cases
print(estimate_deployment_cost(
    instance_count=5,
    hourly_rate=0.45,
    budget_cap=1500.00
))

print(estimate_deployment_cost(
    instance_count=12,
    hourly_rate=0.85,
    budget_cap=5000.00
))