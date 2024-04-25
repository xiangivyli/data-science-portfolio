FROM quay.io/astronomer/astro-runtime:11.1.0

# to run spark in airflow
# 1. Set Spark version and installation directory
ENV SPARK_VERSION=3.5.1
ENV SPARK_HOME=/opt/spark

# 2. Set user id and group id
ARG NEW_UID=1001
ARG NEW_GID=1002

# 3. Switch to root to install packages
USER root

# 4. Set user id and group id
RUN usermod -u $NEW_UID astro && groupmod -g $NEW_GID astro \
    && chown -R astro:astro /usr/local/airflow 

# 5. Install OpenJDK-11
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 6. Install wget and tar to download and extract Spark
RUN apt-get update && apt-get install -y wget tar

# 7. Download and extract Spark to the installation directory
RUN mkdir -p "${SPARK_HOME}" && \
    wget --no-verbose "https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz" -O spark.tgz && \
    tar -xzf spark.tgz -C "${SPARK_HOME}" --strip-components=1 && \
    rm spark.tgz

# 8. Update PATH to include Spark's bin directory
ENV PATH="${SPARK_HOME}/bin:${PATH}"

# 9. Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# 10. Switch back to the astro user for security
USER astro

# to run dbt in airflows
# install dbt into a virtual environment
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-bigquery==1.7.7 && deactivate
