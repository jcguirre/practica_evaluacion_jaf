from azure.cosmos import CosmosClient, exceptions, PartitionKey

Cosmos_endpoint =
cosmos_key =
DATABASE_NAME = 'Evaluacion_DV'
Container_Name_1 = 'Usuarios'
Container_Name_2 = 'Proyectos'

#inicializar el cliente de Cosmos DB
client= CosmosClient(Cosmos_endpoint, cosmos_key)


#Crear o obtener la base de datos
try:
    database = client.create_database_if_not_exists(id=DATABASE_NAME)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(DATABASE_NAME)


#Crear o obtener el contenedor
try:
    container = database.create_container_if_not_exists(
        id=Container_Name_1,
        partition_key={'paths': ['/id'], 'kind': 'Hash'},
        offer_throughput=400
    )
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(Container_Name_1)

try:
    container = database.create_container_if_not_exists(
        id=Container_Name_2,
        partition_key={'paths': ['/id'], 'kind': 'Hash'},
        offer_throughput=400
    )
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(CONTAINER_NAME_2)
