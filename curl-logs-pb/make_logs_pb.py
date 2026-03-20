import time

from opentelemetry.proto.collector.logs.v1 import logs_service_pb2
from opentelemetry.proto.logs.v1 import logs_pb2
from opentelemetry.proto.resource.v1 import resource_pb2
from opentelemetry.proto.common.v1 import common_pb2

def main():
    req = logs_service_pb2.ExportLogsServiceRequest()

    # Resource: service.name = "cribl-goat-demo"
    resource_logs = req.resource_logs.add()
    resource = resource_logs.resource
    resource.attributes.append(
        common_pb2.KeyValue(
            key="service.name",
            value=common_pb2.AnyValue(string_value="cribl-otlp-curl"),
        )
    )

    # Scope + single LogRecord
    scope_logs = resource_logs.scope_logs.add()
    log_record = scope_logs.log_records.add()
    log_record.time_unix_nano = int(time.time() * 1e9)
    log_record.severity_text = "INFO"
    log_record.body.string_value = "Cribl goats are happily herding OTLP logs through your pipelines."

    with open("logs.pb", "wb") as f:
        f.write(req.SerializeToString())

if __name__ == "__main__":
    main()
