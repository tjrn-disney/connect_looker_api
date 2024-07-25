import looker_sdk
import csv

sdk = looker_sdk.init40("looker.ini")
def list_explores_with_caching():
    models = sdk.all_lookml_models()
    explore_caching_info = []
    for model in models:
        print("Models:")
        print(model)
        for explore in model.explores:
            caching_info = {
                'model_name': model.name,
                'explore_name': explore.name
            }
            print("Explore name: ")
            print(explore)
            print("Start looping ")
            for lookml_explore in explore:
                print(lookml_explore)
            print("\n\n\n")
            explore_caching_info.append(caching_info)

    return explore_caching_info

explore_caching_info = list_explores_with_caching()
for info in explore_caching_info:
    print(f"Model: {info['model_name']}, Explore: {info['explore_name']}")
explore_caching_info

filename = "explores_with_caching.csv"

headers = explore_caching_info[0].keys()
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writeheader()
    for explore in explore_caching_info:
        writer.writerow(explore)

print(f"List has been exported to {filename}")
def get_all_datagroups_info():
    # Fetch all data groups
    datagroups = sdk.all_datagroups()

    datagroup_info = []
    for datagroup in datagroups:
        datagroup_info.append({
            'id': datagroup.id,
            'model_name': datagroup.model_name,
            'name': datagroup.name,
            'trigger_value': datagroup.trigger_value,
            'trigger_error': datagroup.trigger_error,
            'stale_before': datagroup.stale_before,
            'trigger_check_at': datagroup.trigger_check_at,
            'triggered_at': datagroup.triggered_at,
            'created_at': datagroup.created_at
        })

    return datagroup_info
def save_to_csv(datagroup_info, filename='datagroups.csv'):
    headers = ['id', 'model_name', 'name', 'trigger_value', 'trigger_error', 'stale_before', 'trigger_check_at',
               'triggered_at', 'created_at']

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in datagroup_info:
            writer.writerow(row)

    print(f'Data groups information saved to {filename}')

datagroup_info = get_all_datagroups_info()
save_to_csv(datagroup_info)

