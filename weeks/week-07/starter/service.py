import grpc
from concurrent import futures
from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
PROTO_DIR = CURRENT_DIR.parent / "proto"
if str(PROTO_DIR) not in sys.path:
    sys.path.insert(0, str(PROTO_DIR))

import service_pb2  # type: ignore[import-not-found]
import service_pb2_grpc  # type: ignore[import-not-found]


class ServiceImplementation(service_pb2_grpc.TicketsServiceServicer):
    def GetTicket(self, request, context):
        return service_pb2.TicketResponse(id=request.id, status="open")

    def CreateTicket(self, request, context):
        return service_pb2.TicketResponse(id=1, status=request.status)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_TicketsServiceServicer_to_server(
        ServiceImplementation(),
        server,
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server is running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
