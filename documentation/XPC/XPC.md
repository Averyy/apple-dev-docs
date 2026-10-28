# XPC

**Framework**: XPC  
**Kind**: module  
**Role**: Framework

Access a low-level interprocess communication mechanism.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 13.0+
- macOS 10.10+

## Overview

XPC provides a lightweight mechanism for basic interprocess communication. It allows you to create lightweight helper tools, called *XPC services*, that perform work on behalf of your app. The `launchd` system daemon manages these services, launching them on demand, shutting them down when idle, and restarting them if they crash. Benefits of XPC services include:

- Centralize work from multiple processes or mediate access to a shared resource.
- Delegate work so it continues beyond a client’s life cycle.
- Privilege isolation to narrow the scope of access for different functionality.

Clients that make use of these services rely on peer-to-peer XPC connections to communicate across process boundaries. There are two sides to each connection. One side, the *listener* or server, responds to incoming connection requests and performs tasks. The other side, the client, initiates connections to an XPC service by creating a *session* with a listener. Once a client establishes a connection to the listener, it sends messages and receives replies from the service.

The type of XPC service you build depends on the requirements of the work it performs. The following table summarizes the types of services available and some differences in how they behave:

| Service Type | Process Environment |
| --- | --- |
| Launch Agent | One process per logged-in user, running as that user. If multiple users log in using fast user switching, each user has their own running process. |
| Launch Daemon | One systemwide process that runs at a higher privilege level, as the `root` user. LaunchDaemons can’t initiate connections to user processes but can respond to requests from them. |
| XPC Service | One process per client of the service, tied to the lifetime of the client. When a client process connects to the service, `launchd` starts a process for the XPC service. When the client process exits, so does the XPC service. You bundle this type of service inside of an app or framework. |

> **Note**:  The LaunchAgent and LaunchDaemon types require special installation and configuration. Prior to macOS 13, apps typically used installation scripts to configure these service types. In macOS 13 and later, the [Service Management](../ServiceManagement/ServiceManagement.md) framework provides a new structure for packaging and installing these service types.

You can build an XPC service using C, Swift, or Objective-C. There are both high- and low-level APIs for using XPC. If your project uses the Foundation framework, [`NSXPCConnection`](../Foundation/nsxpcconnection.md) provides a high-level object-oriented API that enables a transparent remote method dispatch mechanism between processes. Using [`NSXPCConnection`](../Foundation/nsxpcconnection.md) in the Foundation framework lets you design a well-defined protocol for clients to use. If your project doesn’t or can’t link against Foundation, use the lower-level `libSystem` APIs in the XPC framework.

## Topics

### Essentials
- [XPC updates](../Updates/xpc.md)
  Learn about important changes to XPC.
### Interprocess communication
- [Creating XPC services](./creating-xpc-services.md)
  Configure a listener, establish a client session, and exchange messages between processes.
- [class XPCListener](./xpclistener.md)
  A type that performs tasks for clients across process boundaries.
- [class XPCSession](./xpcsession.md)
  A type that sends messages to a server process.
- [struct XPCReceivedMessage](./xpcreceivedmessage.md)
  A type that represents a message sent between a session and a listener.
- [typealias xpc_listener_t](./xpc_listener_t.md)
  A C type that performs tasks for clients across process boundaries.
- [typealias xpc_session_t](./xpc_session_t-10if0.md)
  A C type that sends messages to a server process.
### Tasks
- [XPC activities](./xpc-activities.md)
  Schedule background activities for the system to execute.
### Events
- [XPC events](./xpc-events.md)
  Respond on demand to IOKit events and notifications.
### Additional Types
- [XPC objects](./xpc-objects.md)
  Encapsulate data in objects that represent primitive types, collections, and more.
- [Utilities](./utilities.md)
  Browse debugging utilities and constants to use with the XPC APIs.
- [XPC connections](./xpc-connections.md)
  Create and manage connections to services using connection-based APIs.
### Classes
- [class OS_xpc_session](./os_xpc_session-swift.class.md)
### Structures
- [struct XPCEndpoint](./xpcendpoint.md)
  A connection in serialized form.
- [struct XPCLiteralValue](./xpcliteralvalue.md)
  A type that bridges Swift literal values to XPC objects for use in dictionary literals.
- [struct XPCPeerRequirement](./xpcpeerrequirement.md)
### Type Aliases
- [typealias xpc_peer_requirement_t](./xpc_peer_requirement_t.md)
### Additional types
- [launchd](./launchd.md)
  Browse APIs for interacting with `launchd`.
### Reference
- [Macros](./xpc-macros.md)
  Macros for use with XPC when coding in Objective-C.
### Protocols
- [OS_xpc_peer_requirement](./os_xpc_peer_requirement.md)
- [OS_xpc_session](./os_xpc_session-c.protocol.md)
### Functions
- [xpc_connection_set_peer_requirement](./xpc_connection_set_peer_requirement.md)
- [xpc_listener_set_peer_requirement](./xpc_listener_set_peer_requirement.md)
- [xpc_peer_requirement_create_entitlement_exists](./xpc_peer_requirement_create_entitlement_exists.md)
- [xpc_peer_requirement_create_entitlement_matches_value](./xpc_peer_requirement_create_entitlement_matches_value.md)
- [xpc_peer_requirement_create_lwcr](./xpc_peer_requirement_create_lwcr.md)
- [xpc_peer_requirement_create_platform_identity](./xpc_peer_requirement_create_platform_identity.md)
- [xpc_peer_requirement_create_team_identity](./xpc_peer_requirement_create_team_identity.md)
- [xpc_peer_requirement_match_received_message](./xpc_peer_requirement_match_received_message.md)
- [xpc_session_set_peer_requirement](./xpc_session_set_peer_requirement.md)
### Macros
- [XPC_ABORTLIKE](./xpc_abortlike.md)
- [XPC_ALLOC_SIZE](./xpc_alloc_size.md)
- [XPC_ATTRIBUTE](./xpc_attribute.md)
- [XPC_CONCAT](./xpc_concat.md)
- [XPC_CONCAT_](./xpc_concat_.md)
- [XPC_CONST](./xpc_const.md)
- [XPC_CSTRING](./xpc_cstring.md)
- [XPC_DIAGNOSE_AS](./xpc_diagnose_as.md)
- [XPC_GIVES_REFERENCE](./xpc_gives_reference.md)
- [XPC_NOCONST](./xpc_noconst.md)
- [XPC_PTR_ASSUMES_SINGLE](./xpc_ptr_assumes_single.md)
- [XPC_READ_NONE](./xpc_read_none.md)
- [XPC_RETURNS_ALIGNED](./xpc_returns_aligned.md)
- [XPC_RETURNS_NONNULL](./xpc_returns_nonnull.md)
- [XPC_SINGLE](./xpc_single.md)
- [XPC_SWIFT_SENDABLE](./xpc_swift_sendable.md)
- [XPC_TESTCONST](./xpc_testconst.md)
- [XPC_TESTNORETURN](./xpc_testnoreturn.md)
- [XPC_TRANSACTION_DEPRECATED](./xpc_transaction_deprecated.md)
- [XPC_UNRETAINED](./xpc_unretained.md)
- [XPC_UNSAFE_INDEXABLE](./xpc_unsafe_indexable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/XPC)*