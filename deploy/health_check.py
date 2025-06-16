import xmlrpc.client

if __name__ == "__main__":
    try:
        server = xmlrpc.client.Server("http://localhost:9005/RPC2")
        info = server.supervisor.getAllProcessInfo()
        error_states = list(filter(lambda x: x["state"] != 20, info))
        exit(len(error_states))
    except Exception as e:
        print(e)
        exit(1)
