# xpc_type_t

**Framework**: XPC  
**Kind**: typealias  
**Role**: Type Alias

A type that describes XPC object types.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias xpc_type_t = OpaquePointer
```

```c
typedef const struct _xpc_type_s * xpc_type_t;
```

## See Also

### Objects
- [typealias xpc_object_t](./xpc_object_t.md)
  A type that can describe all XPC objects, including dictionaries, arrays, strings, and numbers.
- [protocol OS_xpc_object](./os_xpc_object.md)
  The interface for an XPC object.
- [class OS_xpc_listener](./os_xpc_listener-swift.class.md)
- [OS_xpc_listener](./os_xpc_listener-c.protocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_type_t)*