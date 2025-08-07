def generate_insights(data):
    fact = data["fact_play_sessions"]
    dim_user = data["dim_user"]
    dim_payment_plan = data["dim_payment_plan"]

    print("\n INSIGHTS")

    # 1. Sessions: Online vs Mobile
    print("\n1. Play sessions by platform:")
    print(fact["channel_code"].value_counts())

    # 2. Payment: One-time vs Subscription
    print("\n2. Registered users by payment frequency:")
    print(dim_user["english_description"].value_counts())

    # 3. Revenue generated
    print("\n3. Estimated gross revenue in 2024:")
    revenue = dim_user["cost_amount"].sum()
    print(f"$ {revenue:,.2f}")