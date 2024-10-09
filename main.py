import typer
import redis
import socket
from typing_extensions import Annotated


app = typer.Typer()
r = redis.Redis(host='localhost', port=6379)


def main(port: Annotated[int, typer.Option()], origin: Annotated[str, typer.Option()]):
    # typer.echo(f"Starting server on port {port} with origin {origin}")
    start_proxy_server(port)

def save_response(response, url):
    r.setex(url, 120, response)

def check_cache(url):
    response = r.get(url)
    if response:
        return response
    return None

def start_proxy_server(port: int):
    # TODO: Implement the proxy server here.
    print("TODO")


if __name__ == "__main__":
    typer.run(main)