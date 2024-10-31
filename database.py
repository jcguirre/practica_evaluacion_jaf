from azure.cosmos import CosmosClient,container



Cosmos_endpoint = 'https://dbjafdev.documents.azure.com:443/'
cosmos_key = 'chFx77YDSmgHgVtHlo4C9gtk1U7nfwHu6sZne5uMNUd6wIayaLTAxD4i3ZtxIdFB3mEp0ciBY2uPACDbzWyHkw=='
DATABASE_NAME = 'Evaluacion_DV'
client = CosmosClient(Cosmos_endpoint, cosmos_key)
Container_Usuarios = client.get_database_client(DATABASE_NAME).get_container_client("Usuarios")
Container_Proyectos = client.get_database_client(DATABASE_NAME).get_container_client("Proyectos")