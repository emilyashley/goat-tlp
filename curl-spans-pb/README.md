Create a logs.pb file:

`pip3 install opentelemetry-proto`

`python3 make_logs_pb.py`


Send a minimal curl test with logs over OTLP HTTP into a Cribl OTel Source:

```
curl -X POST \
'http://<cribl-host>:4318/v1/logs' \
 --header 'Content-Type: application/x-protobuf' \
 --data-binary @logs.pb
```

Add HTTPS and Authorization. Configure TLS, auth, and routing to match your deployment’s requirements:

```
curl -X POST \
'https://<cribl_host>:4318/v1/logs' \
--header 'Content-Type: application/x-protobuf' \
--header 'Authorization: Bearer <TOKEN>' \
--data-binary @logs.pb
```