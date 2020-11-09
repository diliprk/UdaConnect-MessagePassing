## Architectural Design
- The gRPC payload (_person data_) in this case is having static data types (`string`) and does not require any dynamic changing of data types which is supported by REST. gRPC is also faster than REST, when sending and receiving data and thus gRPC was chosen for the `person create` process and this specific payload.

- In addition, the person creation process will happen typically once, whereas the location ingestion process will be continuous as it will be streaming data.

- Kafka is an ideal choice for this location creation service as it is perfectly suited for real time streaming data ingestion. It also has typical applications in the logistics industry to track and monitor location of cars, trucks and shipments in real time.

- The other API endpoints are kept ‘as is’ because they are only to get data from database (to list data) and are not related to ingestion of data.
