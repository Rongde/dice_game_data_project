from etl.extractor import extract_all
from etl.transformer import transform_all
from etl.loader import load_all
from quality.validations import run_quality_checks
from analytics.insights import generate_insights

def main():
    # Step 1: Extract raw datasets
    raw_data = extract_all()

    # Step 2: Transform into fact/dimension star schema
    modeled_data = transform_all(raw_data)

    # Step 3: Run data quality checks(Unite Test)
    run_quality_checks(modeled_data)


    # Step 4: Load transformed data to local warehouse
    load_all(modeled_data)

    # Step 5: Generate insights for the business
    generate_insights(modeled_data)

if __name__ == '__main__':
    main()