import os
import time

from opentelemetry.proto.collector.trace.v1 import trace_service_pb2
from opentelemetry.proto.trace.v1 import trace_pb2  # noqa: F401  (imported for type context)
from opentelemetry.proto.resource.v1 import resource_pb2  # noqa: F401
from opentelemetry.proto.common.v1 import common_pb2

def main():
    req = trace_service_pb2.ExportTraceServiceRequest()

    # Resource: service.name = "cribl-otlp-curl"
    resource_spans = req.resource_spans.add()
    resource = resource_spans.resource
    resource.attributes.append(
        common_pb2.KeyValue(
            key="service.name",
            value=common_pb2.AnyValue(string_value="cribl-otlp-curl"),
        )
    )

    # Scope + single Span
    scope_spans = resource_spans.scope_spans.add()
    span = scope_spans.spans.add()

    now_ns = int(time.time() * 1e9)

    span.trace_id = os.urandom(16)
    span.span_id = os.urandom(8)
    span.name = "curl-otlp-span"
    span.kind = 1  # SPAN_KIND_INTERNAL (optional, but explicit)

    span.start_time_unix_nano = now_ns
    span.end_time_unix_nano = now_ns + 1_000_000  # +1 ms

    # Optional example attribute
    span.attributes.append(
        common_pb2.KeyValue(
            key="otel.test",
            value=common_pb2.AnyValue(string_value="goat-tlp-curl-span"),
        )
    )

    with open("spans.pb", "wb") as f:
        f.write(req.SerializeToString())

if __name__ == "__main__":
    main()