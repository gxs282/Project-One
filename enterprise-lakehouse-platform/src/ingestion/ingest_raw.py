def ingest_raw(source_uri: str, output_path: str) -> None:
    """Placeholder raw ingestion job.

    Replace with connectors/readers (files, APIs, CDC) and write to bronze storage.
    """
    raise NotImplementedError("Implement raw ingestion")


if __name__ == "__main__":
    # Example: ingest_raw("s3://bucket/path", "/mnt/bronze")
    pass
