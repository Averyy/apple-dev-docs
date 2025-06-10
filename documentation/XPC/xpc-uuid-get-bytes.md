# xpc_uuid_get_bytes(_:)

**Framework**: XPC  
**Kind**: func

Copies the UUID that an XPC UUID object boxes into the specified UUID buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_uuid_get_bytes(_ xuuid: xpc_object_t) -> UnsafePointer<UInt8>?
```

#### Return Value

The underlying `uuid_t` bytes. The returned pointer may be safely passed to the `uuid(3)` APIs.

## Parameters

- `xuuid`: The UUID object which is to be examined.

## See Also

- [func xpc_uuid_create(UnsafePointer<UInt8>) -> xpc_object_t](xpc_uuid_create(_:).md)
  Creates an XPC object that represents a universally unique identifier (UUID).


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_uuid_get_bytes(_:))*