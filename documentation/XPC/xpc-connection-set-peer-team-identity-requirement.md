# xpc_connection_set_peer_team_identity_requirement(_:_:)

**Framework**: XPC  
**Kind**: func

Sets a requirement that the executable for the peer process has a valid code signature and is signed by the same team identifier as the calling process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+

## Declaration

```swift
func xpc_connection_set_peer_team_identity_requirement(_ connection: xpc_connection_t, _ signing_identifier: UnsafePointer<CChar>?) -> Int32
```

#### Return Value

On success, `0`. Otherwise, a value from [`Errors`](xpc-connections#Errors.md).

#### Discussion

When you set this requirement on a connection, the operating system checks that peer process satisfies the requirement every time it sends a message to your process.

- If the peer process initiated the connection and its executable isn’t signed by the same team, or doesn’t have the correct signing identifier, then you don’t receive a message and the operating system doesn’t call your event handler.
- If your process sent a message to its peer expecting a reply, and its executable isn’t signed by the same team, or doesn’t have the correct signing identifier, then you don’t receive a reply and the operating system delivers [`XPC_ERROR_PEER_CODE_SIGNING_REQUIREMENT`](xpc_error_peer_code_signing_requirement-c.macro.md) instead.

> ❗ **Important**:  Don’t call this function multiple times for the same connection, or call multiple functions that set code-signing requirements on the same connection. If you use either of these approaches, the system terminates your process with an error.

## Parameters

- `connection`: The XPC connection.
- `signing_identifier`: The code-signing identifier for the peer process’s executable. This value is typically a Bundle ID for apps and extensions. Pass   to indicate that any binary signed by the same team as this process is acceptable.

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
- [func xpc_connection_set_peer_code_signing_requirement(xpc_connection_t, UnsafePointer<CChar>) -> Int32](xpc_connection_set_peer_code_signing_requirement(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_set_peer_team_identity_requirement(_:_:))*