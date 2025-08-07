import os

def load_all(data):
    output_dir = "data/warehouse"
    os.makedirs(output_dir, exist_ok=True)

    for name, df in data.items():
        output_path = os.path.join(output_dir, f"{name}.csv")
        df.to_csv(output_path, index=False)
        print(f"Saved {name} to {output_path}")