# Define the Spark job submission task (repartition parquet locally)
    repartition_parquet = SparkSubmitOperator(
        task_id='repartition_parquet',
        application='/usr/local/airflow/include/spark_repartition_parquet.py', 
        conn_id='spark_default',
        total_executor_cores='1',
        executor_memory='2g',
        num_executors='1',
        driver_memory='2g',
        verbose=False,
        env_vars={'PATH': '/bin:/usr/bin:/usr/local/bin'}
    )

    # Create a task to upload the files to GCS
    upload_parquet_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_parquet_to_gcs',
        src='/usr/local/airflow/include/dataset/parquet/job_postings/*.parquet',
        dst= parquet_folder,
        bucket=bucket,
        gcp_conn_id='gcp',
        mime_type='application/octet-stream',
        )


  # Set dependencies: the Spark job should run after all upload tasks are complete
    start >> upload_raw_tasks >> repartition_parquet >> upload_parquet_to_gcs >> end


upload_raw_tasks = []
    
    for raw_file_path, table in zip(csv_files, table_names):
        task_id = f"upload_raw_{table}_to_gcs"

        dst_raw_path = f"{gcs_raw_folder}/{table}.csv"

        upload_raw_to_gcs = LocalFilesystemToGCSOperator(
            task_id=task_id,
            src=raw_file_path,
            dst=dst_raw_path,
            bucket=bucket,
            gcp_conn_id='gcp',
            mime_type='text/csv',
        )

        upload_raw_tasks.append(upload_raw_to_gcs)