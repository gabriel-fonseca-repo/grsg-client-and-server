import os
import grpc_tools.protoc


def generate_protos(proto_dir, python_out_dir, grpc_python_out_dir, proto_file):
    grpc_tools.protoc.main(
        (
            "",
            f"-I{proto_dir}",
            f"--python_out={python_out_dir}",
            f"--grpc_python_out={grpc_python_out_dir}",
            os.path.join(proto_dir, proto_file),
        )
    )


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    python_out_dir = os.path.join(script_dir, "generated")
    grpc_python_out_dir = os.path.join(script_dir, "generated")

    proto_dir = os.path.join(
        script_dir, os.pardir, os.pardir, "servers/grpc/src/main/proto"
    )
    proto_file = "music-streaming-service.proto"

    os.makedirs(python_out_dir, exist_ok=True)
    os.makedirs(grpc_python_out_dir, exist_ok=True)

    generate_protos(proto_dir, python_out_dir, grpc_python_out_dir, proto_file)
