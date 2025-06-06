# xpc_uuid_create(_:)

**Framework**: Xpc  
**Kind**: func

Creates an XPC object that represents a universally unique identifier (UUID).

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_uuid_create(_ uuid: UnsafePointer<UInt8>) -> xpc_object_t
```

#### Return Value

A new UUID object.

## Parameters

- `uuid`: The UUID which is to be boxed.

## See Also

- [func xpc_uuid_get_bytes(xpc_object_t) -> UnsafePointer<UInt8>?](xpc_uuid_get_bytes(_:).md)
  Copies the UUID that an XPC UUID object boxes into the specified UUID buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_uuid_create(_:))*