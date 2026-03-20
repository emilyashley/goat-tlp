This is a collection of scripts to run a local OpenTelemetry Collector and expose it to the internet so that an
external writer can send example log data for inspection. The Collector configuration has a `debug` exporter (on
detailed output level) to print accepted OTLP/OTLP-HTTP logs.

## Requirements

- [`ngrok`](https://ngrok.com/downloads)
- docker

## Instructions

Run the following commands in separate terminals.

1. Start an ngrok tunnel that forwards to `:4318`.

    ```
    ./ngrok-http.sh
    ```

2. Run the OpenTelemetry Collector which listens on `:4317` (gRPC) and `:4318` (HTTP).

    ```
    ./run-collector.sh
    ```

3. Write Telemetry to remote ngrok tunnel.

    ```
    # Copy the hostname from the "Forwarding" section of the output "ngrok-http.sh" command's output.  
    #
    # For example, in the following output the hostname is "a5889b2be4cc.ngrok-free.app":
    #
    #   Forwarding                    https://a5889b2be4cc.ngrok-free.app -> http://localhost:4318     
    #
    # Apply that hostname in your OpenTelemetry Destination in Cribl Cloud

    ```

4. Review the logs printed in the OpenTelemtry Collector output.
