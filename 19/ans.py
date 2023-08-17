from azure.storage.filedatalake import DataLakeServiceClient

account_name = "your_account_name"
account_key = "your_account_key"
file_system_name = "your_file_system_name"
directory_path = "path/to/your/directory"
file_name = "your_file.txt"
service_client = DataLakeServiceClient(account_url=f"https://{account_name}.dfs.core.windows.net", credential=account_key)
file_system_client = service_client.get_file_system_client(file_system_name)
directory_client = file_system_client.get_directory_client(directory_path)
for item in directory_client.get_paths():
    print(item.name)
file_client = directory_client.get_file_client(file_name)
file_contents = file_client.read()
print(file_contents)
