# xpc_listener_set_peer_code_signing_requirement(_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 14.4+

## Declaration

```swift
func xpc_listener_set_peer_code_signing_requirement(_ listener: xpc_listener_t, _ requirement: UnsafePointer<CChar>) -> Int32
```

```c
extern int xpc_listener_set_peer_code_signing_requirement(xpc_listener_t listener, const char *requirement);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_listener_set_peer_code_signing_requirement(_:_:))*