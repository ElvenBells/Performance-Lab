import json
import sys

def deep_fill_values(test_data, values_map):
    if isinstance(test_data, dict):
        if 'id' in test_data:
            test_id = str(test_data['id'])
            if test_id in values_map:
                test_data['value'] = values_map[test_id]
        if 'values' in test_data:
            for item in test_data['values']:
                deep_fill_values(item, values_map)
    elif isinstance(test_data, list):
        for item in test_data:
            deep_fill_values(item, values_map)

# Основной код
if len(sys.argv) != 4:
    print("Usage: python program.py values.json tests.json report.json")
    sys.exit(1)

values_path, tests_path, report_path = sys.argv[1:4]

try:
    # Загрузка данных
    with open(values_path, 'r', encoding='utf-8') as f:
        values_data = json.load(f)
    
    with open(tests_path, 'r', encoding='utf-8') as f:
        tests_data = json.load(f)

    # Создание словаря значений
    values_map = {str(item['id']): item['value'] for item in values_data['values']}

    # Создание копии структуры тестов
    report_data = json.loads(json.dumps(tests_data))

    # Заполнение значений
    deep_fill_values(report_data, values_map)

    # Сохранение отчета
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)

    print(f"Report successfully generated at {report_path}")

except FileNotFoundError as e:
    print(f"File not found: {e.filename}")
    sys.exit(1)
except json.JSONDecodeError:
    print("Invalid JSON format in input files")
    sys.exit(1)
except KeyError as e:
    print(f"Missing required field in JSON: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)