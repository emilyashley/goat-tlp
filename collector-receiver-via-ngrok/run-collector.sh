#!/usr/bin/env bash

set -euo pipefail

docker run \
    -v "$(pwd)/collector.yaml:/etc/otelcol-contrib/config.yaml" \
    -p 127.0.0.1:4317:4317 \
    -p 127.0.0.1:4318:4318 \
    otel/opentelemetry-collector-contrib:0.128.0 \
    2>&1 | tee collector-output.txt
