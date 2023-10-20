import sys
import json
import pandas as pd
user_details = []
def process_json_data(json_data):
    data = json.load(json_data)
    # print(data)
    # for x in data:
    #     print(x['language'])
    user_details.extend(
        [
            {
                'language':x['language'],
            }
        for x in data])
    print(user_details)

if __name__ == "__main__":
    try:
        process_json_data(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {str(e)}")
        sys.exit(1)
