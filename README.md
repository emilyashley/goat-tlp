# goat-tlp
A small pasture of utilities for navigating OpenTelemetry and Cribl

- [collector-receiver-via-ngrok](#collector-receiver-via-ngrok)  - run a local OpenTelemetry Collector and expose it via ngrok so external senders (like Cribl) can write OTLP traffic, useful for otlp spec & integration testing
- [curl-logs-pb](#curl-logs-pb) - little Python helper and example curl commands to generate a logs.pb OTLP payload and send it to a Cribl OpenTelemetry Source over HTTP/HTTPS for testing connectivity.
- [otel-demo-cribl-config-extras](#otel-demo-cribl-config-extras) - example otelcol-config-extras.yml for the OpenTelemetry Demo’s Docker deployment, wired to export OTLP logs, metrics, and traces into Cribl (a nice “practice pasture” for your telemetry goats).