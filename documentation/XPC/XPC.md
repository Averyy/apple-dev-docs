# XPC

**Framework**: XPC  
**Kind**: module

Access a low-level interprocess communication mechanism.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 13.0+
- macOS 10.10+

#### Overview

XPC provides a lightweight mechanism for basic interprocess communication. It allows you to create lightweight helper tools, called , that perform work on behalf of your app. The `launchd` system daemon manages these services, launching them on demand, shutting them down when idle, and restarting them if they crash. Benefits of XPC services include:

- Centralize work from multiple processes or mediate access to a shared resource.
- Delegate work so it continues beyond a client’s life cycle.
- Privilege isolation to narrow the scope of access for different functionality.

Clients that make use of these services rely on peer-to-peer XPC connections to communicate across process boundaries. There are two sides to each connection. One side, the  or server, responds to incoming connection requests and performs tasks. The other side, the client, initiates connections to an XPC service by creating a  with a listener. Once a client establishes a connection to the listener, it sends messages and receives replies from the service.

The type of XPC service you build depends on the requirements of the work it performs. The following table summarizes the types of services available and some differences in how they behave:

| Service Type | Process Environment |
| --- | --- |
| Launch Agent | One process per logged-in user, running as that user. If multiple users log in using fast user switching, each user has their own running process. |
| Launch Daemon | One systemwide process that runs at a higher privilege level, as the `root` user. LaunchDaemons can’t initiate connections to user processes but can respond to requests from them. |
| XPC Service | One process per client of the service, tied to the lifetime of the client. When a client process connects to the service, `launchd` starts a process for the XPC service. When the client process exits, so does the XPC service. You bundle this type of service inside of an app or framework. |

> **Note**:  The LaunchAgent and LaunchDaemon types require special installation and configuration. Prior to macOS 13, apps typically used installation scripts to configure these service types. In macOS 13 and later, the [`Service Management`](https://developer.apple.com/documentation/ServiceManagement) framework provides a new structure for packaging and installing these service types.

You can build an XPC service using C, Swift, or Objective-C. There are both high- and low-level APIs for using XPC. If your project uses the Foundation framework, [`NSXPCConnection`](https://developer.apple.com/documentation/Foundation/NSXPCConnection) provides a high-level object-oriented API that enables a transparent remote method dispatch mechanism between processes. Using [`NSXPCConnection`](https://developer.apple.com/documentation/Foundation/NSXPCConnection) in the Foundation framework lets you design a well-defined protocol for clients to use. If your project doesn’t or can’t link against Foundation, use the lower-level `libSystem` APIs in the XPC framework.

## Topics

### Essentials
- [XPC updates](../Updates/XPC.md)
  Learn about important changes to XPC.
### Interprocess communication
- [Creating XPC services](creating-xpc-services.md)
  Configure a listener, establish a client session, and exchange messages between processes.
- [class XPCListener](xpclistener.md)
  A type that performs tasks for clients across process boundaries.
- [class XPCSession](xpcsession.md)
  A type that sends messages to a server process.
- [struct XPCReceivedMessage](xpcreceivedmessage.md)
  A type that represents a message sent between a session and a listener.
- [typealias xpc_listener_t](xpc_listener_t.md)
  A C type that performs tasks for clients across process boundaries.
- [typealias xpc_session_t](xpc_session_t-10if0.md)
  A C type that sends messages to a server process.
### Tasks
- [XPC activities](xpc-activities.md)
  Schedule background activities for the system to execute.
### Events
- [XPC events](xpc-events.md)
  Respond on demand to IOKit events and notifications.
### Additional Types
- [XPC objects](xpc-objects.md)
  Encapsulate data in objects that represent primitive types, collections, and more.
- [Utilities](utilities.md)
  Browse debugging utilities and constants to use with the XPC APIs.
- [XPC connections](xpc-connections.md)
  Create and manage connections to services using connection-based APIs.
### Classes
- [class OS_xpc_session](os_xpc_session-swift.class.md)
### Structures
- [struct XPCPeerRequirement](xpcpeerrequirement.md)
### Type Aliases
- [typealias xpc_peer_requirement_t](xpc_peer_requirement_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/XPC)*