# xpc_retain(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 4.0+ - Deprecated in 17.4
- macOS 10.7+ - Deprecated in 14.4

> **Deprecated**: Use Swift’s automatic reference counting to manage the lifetime of XPC objects

## Declaration

```swift
func xpc_retain(_ object: xpc_object_t) -> xpc_object_t
```

## See Also

### Object life cycle
- [func xpc_release(xpc_object_t)](./xpc_release%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_retain(_:))*