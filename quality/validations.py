import pandas as pd


def check_no_nulls(df: pd.DataFrame, columns: list[str], table_name: str):
    for col in columns:
        null_count = df[col].isnull().sum()
        if null_count > 0:
            raise ValueError(f"[{table_name}] Column '{col}' has {null_count} null values.")

def check_unique_key(df: pd.DataFrame, key_columns: list[str], table_name: str):
    duplicated = df.duplicated(subset=key_columns).sum()
    if duplicated > 0:
        raise ValueError(f"[{table_name}] Found {duplicated} duplicate rows for key {key_columns}.")


def validate_fact_play_sessions(df: pd.DataFrame):
    check_no_nulls(df, ["user_id", "channel_code", "status_code", "start_datetime", "end_datetime"], "fact_play_sessions")


def validate_dim_user(df: pd.DataFrame):
    check_unique_key(df, ["user_id"], "dim_user")
    check_no_nulls(df, ["username"], "dim_user")


def validate_dim_channel(df: pd.DataFrame):
    check_unique_key(df, ["channel_code"], "dim_channel")
    check_no_nulls(df, ["english_description"], "dim_channel")


def validate_dim_status(df: pd.DataFrame):
    check_unique_key(df, ["status_code"], "dim_status")
    check_no_nulls(df, ["english_description"], "dim_status")


def validate_dim_payment_plan(df: pd.DataFrame):
    check_unique_key(df, ["plan_id"], "dim_payment_plan")
    check_no_nulls(df, ["payment_frequency_code", "cost_amount"], "dim_payment_plan")


def run_quality_checks(model: dict[str, pd.DataFrame]):
    validate_fact_play_sessions(model["fact_play_sessions"])
    print("pass validate_fact_play_sessions quality_checks")
    validate_dim_user(model["dim_user"])
    print("pass dim_user quality_checks")
    validate_dim_channel(model["dim_channel"])
    print("pass dim_channel quality_checks")
    validate_dim_status(model["dim_status"])
    print("pass dim_status quality_checks")
    validate_dim_payment_plan(model["dim_payment_plan"])
    print("pass quality_checks")
