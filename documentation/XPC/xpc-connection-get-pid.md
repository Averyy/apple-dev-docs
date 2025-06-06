# xpc_connection_get_pid(_:)

**Framework**: Xpc  
**Kind**: func

Returns the PID of the remote peer.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func xpc_connection_get_pid(_ connection: xpc_connection_t) -> pid_t
```

#### Return Value

The PID of the remote peer.

#### Discussion

A given PID is not guaranteed to be unique across an entire boot cycle. Great care should be taken when dealing with this information, as it can go stale after the connection is established. macOS recycles PIDs, and therefore another process could spawn and claim the PID before a message is actually received from the connection.

XPC will deliver an error to your event handler if the remote process goes away, but there are no guarantees as to the timing of this notification’s delivery either at the kernel layer or at the XPC layer.

## Parameters

- `connection`: The connection object which is to be examined.

## See Also

- [func xpc_connection_get_name(xpc_connection_t) -> UnsafePointer<CChar>?](xpc_connection_get_name(_:).md)
  Returns the name of the remote service that creates the connection.
- [func xpc_connection_get_euid(xpc_connection_t) -> uid_t](xpc_connection_get_euid(_:).md)
  Returns the EUID of the remote peer.
- [func xpc_connection_get_egid(xpc_connection_t) -> gid_t](xpc_connection_get_egid(_:).md)
  Returns the EGID of the remote peer.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_get_pid(_:))*