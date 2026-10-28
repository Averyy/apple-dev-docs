# xpc_uuid_get_bytes(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Copies the UUID that an XPC UUID object boxes into the specified UUID buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func xpc_uuid_get_bytes(_ xuuid: xpc_object_t) -> UnsafePointer<UInt8>?
```

```c
extern const uint8_t *xpc_uuid_get_bytes(xpc_object_t xuuid);
```

## Return Value

The underlying `uuid_t` bytes. The returned pointer may be safely passed to the `uuid(3)` APIs.

## Parameters

- `xuuid`: The UUID object which is to be examined.

## See Also

### UUID objects
- [func xpc_uuid_create(UnsafePointer<UInt8>) -> xpc_object_t](./xpc_uuid_create%28_%29.md)
  Creates an XPC object that represents a universally unique identifier (UUID).


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_uuid_get_bytes(_:))*