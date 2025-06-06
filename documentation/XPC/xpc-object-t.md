# xpc_object_t

**Framework**: Xpc  
**Kind**: typealias

A type that can describe all XPC objects, including dictionaries, arrays, strings, and numbers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias xpc_object_t = any OS_xpc_object
```

#### Discussion

XPC objects are created with a retain count of 1, and therefore it is the caller’s responsibility to call [`xpc_release`](xpc_release.md) on them when they are no longer needed.

## See Also

- [typealias xpc_type_t](xpc_type_t.md)
  A type that describes XPC object types.
- [protocol OS_xpc_object](os_xpc_object.md)
  The interface for an XPC object.
- [class OS_xpc_listener](os_xpc_listener-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_object_t)*