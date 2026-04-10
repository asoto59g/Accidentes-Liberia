import json
import os

years = [2020, 2021, 2022, 2023, 2024]

for year in years:
    input_file = f'Accidentes{year}.geojson'
    output_file = f'liberia_{year}.js'
    
    if not os.path.exists(input_file):
        print(f"Skipping {input_file} (not found)")
        continue
        
    print(f"Processing {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    liberia_features = [
        f for f in data.get('features', [])
        if f.get('properties', {}).get('nombrecanton') == 'Liberia'
    ]

    print(f"Found {len(liberia_features)} features for {year}.")

    output_data = {
        "type": "FeatureCollection",
        "features": liberia_features
    }

    variable_name = f"COSEVI_DATA_{year}"
    with open(output_file, 'w', encoding='utf-8') as f:
        # Convert to a JS variable
        json_str = json.dumps(output_data, ensure_ascii=False)
        f.write(f"var {variable_name} = {json_str};")

    print(f"Saved to {output_file}")

print("Extraction complete.")
