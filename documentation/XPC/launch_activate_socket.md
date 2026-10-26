# launch_activate_socket

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Retrieves the file descriptors for sockets in the process’s `launchd` property list.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.10+

## Declaration

```c
extern int launch_activate_socket(const char *name, int **fds, size_t *cnt);
```

#### Return Value

On success, `0` is returned. Otherwise, an appropriate POSIX-domain is returned.

#### Discussion

The possible error codes are:

- `ENOENT` — There was no socket of the specified name owned by the caller.
- `ESRCH` — The caller isn’t a process managed by launchd.
- `EALREADY` — The socket has already been activated by the caller.

## Parameters

- `name`: The name of the socket entry in the service’s Sockets dictionary.
- `fds`: On return, this parameter is populated with an array of file descriptors. One socket can have many descriptors associated with it depending on the characteristics of the network interfaces on the system. The descriptors in this array are the results of calling `getaddrinfo(3)` with the parameters described in `launchd.plist`. The caller is responsible for calling `free(3)` on the returned pointer.
- `cnt`: The number of file descriptor entries in the returned array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/launch_activate_socket)*