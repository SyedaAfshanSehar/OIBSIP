# OIBSIP Python Task 5 — Chat Application

## Beginner tier
A local client/server chat application using Python sockets and threading.

### Features
- Server listens on localhost.
- Client connects to the server.
- Two or more clients can exchange messages in real time.
- User names are shown with messages.
- Join/disconnect notifications are broadcast.
- Multiple clients are handled with threads.

## Run the demo
Open three terminals.

### Terminal 1 — server
```bash
python server.py
```

### Terminal 2 — client 1
```bash
python client.py
```

Enter a name and send a message.

### Terminal 3 — client 2
```bash
python client.py
```

Enter a different name and send a message. Messages should appear in both clients.

Use `/quit` to leave.
