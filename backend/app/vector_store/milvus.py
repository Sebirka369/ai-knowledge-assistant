from pymilvus import DataType, MilvusClient


class MilvusStore:

    COLLECTION_NAME = "document_chunks"
    EMBEDDING_DIMENSION = 384

    def __init__(
        self,
        uri: str = "http://localhost:19530",
    ):
        self.client = MilvusClient(
            uri=uri
        )

    def create_collection(self):
        if self.client.has_collection(
            collection_name=self.COLLECTION_NAME
        ):
            return

        schema = self.client.create_schema(
            auto_id=True,
            enable_dynamic_field=False,
        )

        schema.add_field(
            field_name="id",
            datatype=DataType.INT64,
            is_primary=True,
        )

        schema.add_field(
            field_name="chunk_id",
            datatype=DataType.VARCHAR,
            max_length=36,
        )

        schema.add_field(
            field_name="document_id",
            datatype=DataType.VARCHAR,
            max_length=36,
        )

        schema.add_field(
            field_name="chunk_index",
            datatype=DataType.INT64,
        )

        schema.add_field(
            field_name="embedding",
            datatype=DataType.FLOAT_VECTOR,
            dim=self.EMBEDDING_DIMENSION,
        )

        self.client.create_collection(
            collection_name=self.COLLECTION_NAME,
            schema=schema,
        )

    def drop_collection(self):
        if self.client.has_collection(
            collection_name=self.COLLECTION_NAME
        ):
            self.client.drop_collection(
                collection_name=self.COLLECTION_NAME
            )

    def create_index(self):
        index_params = self.client.prepare_index_params()

        index_params.add_index(
            field_name="embedding",
            index_type="AUTOINDEX",
            metric_type="COSINE",
        )

        self.client.create_index(
            collection_name=self.COLLECTION_NAME,
            index_params=index_params,
        )

    def load_collection(self):
        self.client.load_collection(
            collection_name=self.COLLECTION_NAME
        )
    def delete_by_chunk_id(
        self,
        chunk_id: str,
    ):
        return self.client.delete(
            collection_name=self.COLLECTION_NAME,
            filter=f'chunk_id == "{chunk_id}"',
        )
    def insert_chunk(
        self,
        chunk_id: str,
        document_id: str,
        chunk_index: int,
        embedding: list[float],
    ):
        data = [
            {
                "chunk_id": chunk_id,
                "document_id": document_id,
                "chunk_index": chunk_index,
                "embedding": embedding,
            }
        ]

        return self.client.insert(
            collection_name=self.COLLECTION_NAME,
            data=data,
        )

    def search(
        self,
        query_embedding: list[float],
        limit: int = 5,
    ):
        results = self.client.search(
            collection_name=self.COLLECTION_NAME,
            data=[query_embedding],
            anns_field="embedding",
            limit=limit,
            search_params={
                "metric_type": "COSINE",
            },
            output_fields=[
                "chunk_id",
                "document_id",
                "chunk_index",
            ],
        )

        return results
