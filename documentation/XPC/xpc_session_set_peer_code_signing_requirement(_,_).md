# xpc_session_set_peer_code_signing_requirement(_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 14.4+

## Declaration

```swift
func xpc_session_set_peer_code_signing_requirement(_ session: xpc_session_t, _ requirement: UnsafePointer<CChar>) -> Int32
```

```c
extern int xpc_session_set_peer_code_signing_requirement(xpc_session_t session, const char *requirement);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_set_peer_code_signing_requirement(_:_:))*