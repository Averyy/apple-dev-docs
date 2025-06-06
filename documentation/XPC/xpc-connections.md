# XPC connections

**Framework**: Xpc

Create and manage connections to services using connection-based APIs.

#### Overview

Use these APIs to work with XPC connections and related types — for example, when a framework function that you call returns an [`xpc_connection_t`](xpc_connection_t.md).

But, in most situations, the listener- and session-based APIs are a better choice for designing XPC communication protocols. For more information, see [`Creating XPC services`](creating-xpc-services.md).

## Topics

### Creation
- [typealias xpc_connection_t](xpc_connection_t.md)
  A type that represents a connection to a named service.
- [func xpc_connection_create(UnsafePointer<CChar>?, dispatch_queue_t?) -> xpc_connection_t](xpc_connection_create(_:_:).md)
  Creates a new connection object.
- [func xpc_connection_create_from_endpoint(xpc_endpoint_t) -> xpc_connection_t](xpc_connection_create_from_endpoint(_:).md)
  Creates a new connection from the specified endpoint.
- [func xpc_connection_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, UInt64) -> xpc_connection_t](xpc_connection_create_mach_service(_:_:_:).md)
  Creates a new connection object that represents a Mach service.
- [func xpc_connection_set_target_queue(xpc_connection_t, dispatch_queue_t?)](xpc_connection_set_target_queue(_:_:).md)
  Sets the target queue of the connection.
- [var XPC_CONNECTION_MACH_SERVICE_LISTENER: Int32](xpc_connection_mach_service_listener.md)
  A flag that indicates the caller is the listener for the named service.
- [var XPC_CONNECTION_MACH_SERVICE_PRIVILEGED: Int32](xpc_connection_mach_service_privileged.md)
  A flag that indicates the job advertising the service name belongs to a launch daemon rather than a launch agent.
### Event handling
- [func xpc_connection_set_event_handler(xpc_connection_t, xpc_handler_t)](xpc_connection_set_event_handler(_:_:).md)
  Sets the event handler block for the connection.
- [typealias xpc_handler_t](xpc_handler_t.md)
  The type of block that the XPC connection APIs accept.
- [typealias xpc_connection_handler_t](xpc_connection_handler_t.md)
  The type of the function to invoke for a bundled XPC service when there’s a new connection on the service.
### Life cycle
- [func xpc_main(xpc_connection_handler_t) -> Never](xpc_main(_:).md)
  Starts listening for incoming connections and processes them with the specified event handler.
- [func xpc_connection_activate(xpc_connection_t)](xpc_connection_activate(_:).md)
  Activates a new connection.
- [func xpc_connection_suspend(xpc_connection_t)](xpc_connection_suspend(_:).md)
  Suspends the connection so the event handler block doesn’t fire and the connection doesn’t attempt to send any messages it has in its queue.
- [func xpc_connection_resume(xpc_connection_t)](xpc_connection_resume(_:).md)
  Resumes a suspended connection.
- [func xpc_connection_cancel(xpc_connection_t)](xpc_connection_cancel(_:).md)
  Cancels the connection and ensures that its event handler doesn’t fire again.
- [func xpc_transaction_begin()](xpc_transaction_begin().md)
  Informs the XPC runtime when a transaction begins, indicating that the service isn’t idle.
- [func xpc_transaction_end()](xpc_transaction_end().md)
  Informs the XPC runtime when a transaction ends.
- [func xpc_connection_copy_invalidation_reason(xpc_connection_t) -> UnsafeMutablePointer<CChar>?](xpc_connection_copy_invalidation_reason(_:).md)
### Messages
- [func xpc_connection_send_message(xpc_connection_t, xpc_object_t)](xpc_connection_send_message(_:_:).md)
  Sends a message over the connection to the destination service.
- [func xpc_connection_send_barrier(xpc_connection_t, () -> Void)](xpc_connection_send_barrier(_:_:).md)
  Issues a barrier against the connection’s message-send activity.
- [func xpc_connection_send_message_with_reply(xpc_connection_t, xpc_object_t, dispatch_queue_t?, xpc_handler_t)](xpc_connection_send_message_with_reply(_:_:_:_:).md)
  Sends a message over the connection to the destination service and associates a handler to invoke when the remote service sends a reply message.
- [func xpc_connection_send_message_with_reply_sync(xpc_connection_t, xpc_object_t) -> xpc_object_t](xpc_connection_send_message_with_reply_sync(_:_:).md)
  Sends a message over the connection and blocks the caller until it receives a reply.
- [func xpc_main(xpc_connection_handler_t) -> Never](xpc_main(_:).md)
  Starts listening for incoming connections and processes them with the specified event handler.
### Remote peer information
- [func xpc_connection_get_name(xpc_connection_t) -> UnsafePointer<CChar>?](xpc_connection_get_name(_:).md)
  Returns the name of the remote service that creates the connection.
- [func xpc_connection_get_euid(xpc_connection_t) -> uid_t](xpc_connection_get_euid(_:).md)
  Returns the EUID of the remote peer.
- [func xpc_connection_get_egid(xpc_connection_t) -> gid_t](xpc_connection_get_egid(_:).md)
  Returns the EGID of the remote peer.
- [func xpc_connection_get_pid(xpc_connection_t) -> pid_t](xpc_connection_get_pid(_:).md)
  Returns the PID of the remote peer.
- [func xpc_connection_get_asid(xpc_connection_t) -> au_asid_t](xpc_connection_get_asid(_:).md)
  Returns the audit session identifier of the remote peer.
- [func xpc_connection_set_peer_entitlement_exists_requirement(xpc_connection_t, UnsafePointer<CChar>) -> Int32](xpc_connection_set_peer_entitlement_exists_requirement(_:_:).md)
  Sets a requirement that the executable for the peer process has a valid code signature that contains an entitlement.
- [func xpc_connection_set_peer_entitlement_matches_value_requirement(xpc_connection_t, UnsafePointer<CChar>, xpc_object_t) -> Int32](xpc_connection_set_peer_entitlement_matches_value_requirement(_:_:_:).md)
  Sets a requirement that the executable for the peer process has a valid code signature that contains an entitlement with a specific value.
- [func xpc_connection_set_peer_lightweight_code_requirement(xpc_connection_t, xpc_object_t) -> Int32](xpc_connection_set_peer_lightweight_code_requirement(_:_:).md)
  Sets a requirement that the executable for the peer process has a valid code signature that matches the lightweight code requirement.
- [func xpc_connection_set_peer_platform_identity_requirement(xpc_connection_t, UnsafePointer<CChar>?) -> Int32](xpc_connection_set_peer_platform_identity_requirement(_:_:).md)
  Sets a requirement that the executable for the peer process has a valid code signature that identifies it as an Apple-signed binary with the given signing identifier.
- [func xpc_connection_set_peer_team_identity_requirement(xpc_connection_t, UnsafePointer<CChar>?) -> Int32](xpc_connection_set_peer_team_identity_requirement(_:_:).md)
  Sets a requirement that the executable for the peer process has a valid code signature and is signed by the same team identifier as the calling process.
- [func xpc_connection_set_peer_code_signing_requirement(xpc_connection_t, UnsafePointer<CChar>) -> Int32](xpc_connection_set_peer_code_signing_requirement(_:_:).md)
### Context
- [func xpc_connection_set_context(xpc_connection_t, UnsafeMutableRawPointer?)](xpc_connection_set_context(_:_:).md)
  Sets a context on the connection.
- [func xpc_connection_get_context(xpc_connection_t) -> UnsafeMutableRawPointer?](xpc_connection_get_context(_:).md)
  Returns the context for the connection.
- [func xpc_connection_set_finalizer_f(xpc_connection_t, xpc_finalizer_t?)](xpc_connection_set_finalizer_f(_:_:).md)
  Sets the finalizer for the connection.
- [typealias xpc_finalizer_t](xpc_finalizer_t.md)
  A function to invoke when tearing down a connection and freeing its context.
### Endpoints
- [func xpc_endpoint_create(xpc_connection_t) -> xpc_endpoint_t](xpc_endpoint_create(_:).md)
  Creates a new endpoint from a connection that is suitable for embedding into messages.
- [typealias xpc_endpoint_t](xpc_endpoint_t.md)
  A type that represents a connection in serialized form.
### Errors
- [var XPC_ERROR_CONNECTION_INVALID: xpc_object_t](xpc_error_connection_invalid-swift.var.md)
  An error that sends to the connection’s event handler to indicate that the connection is no longer usable.
- [var XPC_ERROR_CONNECTION_INTERRUPTED: xpc_object_t](xpc_error_connection_interrupted-swift.var.md)
  An error that sends to the connection’s event handler when the remote service exits.
- [var XPC_ERROR_TERMINATION_IMMINENT: xpc_object_t](xpc_error_termination_imminent-swift.var.md)
  An error that sends to a peer connection’s event handler when the XPC runtime determines that the program needs to exit and that all outstanding transactions must wind down.

## See Also

- [XPC objects](xpc-objects.md)
  Encapsulate data in objects that represent primitive types, collections, and more.
- [Utilities](utilities.md)
  Browse debugging utilities and constants to use with the XPC APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc-connections)*