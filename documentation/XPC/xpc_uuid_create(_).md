# xpc_uuid_create(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Creates an XPC object that represents a universally unique identifier (UUID).

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
func xpc_uuid_create(_ uuid: UnsafePointer<UInt8>) -> xpc_object_t
```

```c
extern xpc_object_txpc_uuid_create(const uuid_t uuid);
```

## Return Value

A new UUID object.

## Parameters

- `uuid`: The UUID which is to be boxed.

## See Also

### UUID objects
- [func xpc_uuid_get_bytes(xpc_object_t) -> UnsafePointer<UInt8>?](./xpc_uuid_get_bytes%28_%29.md)
  Copies the UUID that an XPC UUID object boxes into the specified UUID buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_uuid_create(_:))*