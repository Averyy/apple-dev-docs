# xpc_connection_set_peer_code_signing_requirement(_:_:)

**Framework**: Xpc  
**Kind**: func

**Availability**:
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func xpc_connection_set_peer_code_signing_requirement(_ connection: xpc_connection_t, _ requirement: UnsafePointer<CChar>) -> Int32
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_set_peer_code_signing_requirement(_:_:))*