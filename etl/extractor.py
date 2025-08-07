import pandas as pd
import os

def extract_all():
    base_path = "data/raw"

    return {
        "user_play_session": pd.read_csv(os.path.join(base_path, "user_play_session.csv")),
        "user_payment_detail": pd.read_csv(os.path.join(base_path, "user_payment_detail.csv")),
        "plan": pd.read_csv(os.path.join(base_path, "plan.csv")),
        "plan_payment_frequency": pd.read_csv(os.path.join(base_path, "plan_payment_frequency.csv")),
        "channel_code": pd.read_csv(os.path.join(base_path, "channel_code.csv")),
        "status_code": pd.read_csv(os.path.join(base_path, "status_code.csv")),
        "user_plan": pd.read_csv(os.path.join(base_path, "user_plan.csv")),
        "user_registration": pd.read_csv(os.path.join(base_path, "user_registration.csv")),
        "user": pd.read_csv(os.path.join(base_path, "user.csv")),
    }