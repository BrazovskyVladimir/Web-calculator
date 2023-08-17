from server import create_server

main_server = create_server()

if __name__ == '__main__':
    main_server.run(host='0.0.0.0')
