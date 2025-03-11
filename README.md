# StreamLine Data Pipeline

## Overview
StreamLine Data Pipeline is a data engineering project that sets up a robust and scalable pipeline using Confluent's Kafka ecosystem. The solution integrates essential services for managing, monitoring, and orchestrating real-time data streams, ensuring data integrity and facilitating data analysis.


## Architecture
The architecture consists of the following components:
- **Zookeeper**: Manages and coordinates the Kafka brokers.
- **Kafka Broker**: Handles the message streaming.
- **Schema Registry**: Manages the schemas for Kafka messages.
- **Control Center**: Provides a UI to monitor and manage the Kafka ecosystem.
- **Airflow**: Manages and schedules data pipelines.

## Services
1. **Zookeeper**
   - Image: `confluentinc/cp-zookeeper:7.9.0`
   - Port: `2181`
2. **Kafka Broker**
   - Image: `confluentinc/cp-server:7.9.0`
   - Ports: `9092`, `9101`
3. **Schema Registry**
   - Image: `confluentinc/cp-schema-registry:7.9.0`
   - Port: `8081`
4. **Control Center**
   - Image: `confluentinc/cp-enterprise-control-center:7.9.0`
   - Port: `9021`
5. **Airflow**
   - Image: `apache/airflow:2.10.5`
   - Port: `8080`

## How to Start
1. Ensure Docker and Docker Compose are installed on your machine.
2. Navigate to the project directory.
3. Run the following commands to build and start the services:
   ```sh
   make build
   make up
   ```
4. Verify the services are running:
   - Control Center: `localhost:9021`
   - Airflow: `localhost:8080`

5. Access the Airflow DAGs, execute them, and verify that the topics and messages have been successfully created in Control Center.

## Objectives
- Set up a scalable and reliable data streaming platform.
- Manage and monitor Kafka clusters using Confluent Control Center.
- Ensure data integrity and schema management with Schema Registry.
- Schedule and manage data pipelines using Airflow.

## References
- [Confluent Documentation](https://docs.confluent.io/)
- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Airflow Documentation](https://airflow.apache.org/docs/)

