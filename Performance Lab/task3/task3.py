import sys
import json

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

with open(values_file, 'r', encoding='utf-8') as f:
    values_data = json.load(f)

with open(tests_file, 'r', encoding='utf-8') as f:
    tests_data = json.load(f)

values_dict = {item['id']: item['value'] for item in values_data['values']}

def fill_values(tests, values):
    for test in tests:
        if 'id' in test and test['id'] in values:
            test['value'] = values[test['id']]
        if 'values' in test:
            fill_values(test['values'], values)

fill_values(tests_data['tests'], values_dict)

with open(report_file, 'w', encoding='utf-8') as f:
    json.dump(tests_data, f, ensure_ascii=False, indent=2)
