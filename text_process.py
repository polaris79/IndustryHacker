import json

def extract_headlines(json_file_path, output_file_path):
    """Extracts headline values from a JSON file with one JSON object per line and saves them to a text file.

    Args:
        json_file_path: Path to the input JSON file.
        output_file_path: Path to the output text file.
    """

    try:
        with open(json_file_path, 'r') as json_file, open(output_file_path, 'w') as output_file:
            for line in json_file:  # Process each line in the file
                try:
                    data = json.loads(line)
                    if "headline" in data:
                        output_file.write(data["headline"] + '\n')
                except json.JSONDecodeError:  # Handle invalid JSON on a line
                    print(f"Warning: Skipping invalid JSON line: {line}")
                except KeyError:  # Handle missing "headline" key
                    print(f"Warning: 'headline' key not found in: {line}")

        print(f"Headlines extracted successfully and saved to {output_file_path}")

    except FileNotFoundError:
        print(f"Error: File not found at {json_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
json_file_path = "News_Category_Dataset_v3.json"  # Replace with your JSON file path
output_file_path = "headlines.txt"  # Replace with desired output file path

extract_headlines(json_file_path, output_file_path)
