import pandas as pd

def transform_all(raw):
    # Clean play session data
    session_df = raw["user_play_session"].copy()
    session_df["start_datetime"] = pd.to_datetime(session_df["start_datetime"])
    session_df["end_datetime"] = pd.to_datetime(session_df["end_datetime"])
    session_df["duration_minutes"] = (session_df["end_datetime"] - session_df["start_datetime"]).dt.total_seconds() / 60
    session_df["session_date"] = session_df["start_datetime"].dt.date
    fact_play_sessions = session_df

    # Channel dimension
    dim_channel = raw["channel_code"].rename(columns={"play_session_channel_code": "channel_code"})

    # Status dimension
    dim_status = raw["status_code"].rename(columns={"play_session_status_code": "status_code"})

    # Payment Plan dimension
    dim_payment_plan = pd.merge(
        raw["plan"],
        raw["plan_payment_frequency"],
        on="payment_frequency_code",
        how="left"
    )

    # User dimension
    dim_user = pd.merge(raw["user"], raw["user_registration"], on="user_id", how="inner")
    dim_user = pd.merge(dim_user, raw["user_plan"], on="user_registration_id", how="left")
    dim_user = pd.merge(dim_user, dim_payment_plan, on="plan_id", how="left")
    dim_user = pd.merge(dim_user, raw["user_payment_detail"], on="payment_detail_id", how="left")
    dim_user = dim_user.rename(columns={"email_x": "user_email"})
    dim_user = dim_user.rename(columns={"email_y": "user_registration_email"})
    dim_user = dim_user.drop_duplicates(subset=["user_id"])

    return {
        "fact_play_sessions": fact_play_sessions,
        "dim_channel": dim_channel,
        "dim_status": dim_status,
        "dim_payment_plan": dim_payment_plan,
        "dim_user": dim_user
    }
