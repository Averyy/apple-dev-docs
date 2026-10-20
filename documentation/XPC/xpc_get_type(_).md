# xpc_get_type(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Returns the type of an object.

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
func xpc_get_type(_ object: xpc_object_t) -> xpc_type_t
```

```c
extern xpc_type_txpc_get_type(xpc_object_t object);
```

#### Return Value

An opaque pointer describing the type of the object. This pointer is suitable for direct comparison to exported type constants with the equality operator.

## Parameters

- `object`: The object to examine.

## See Also

### Identity
- [func xpc_type_get_name(xpc_type_t) -> UnsafePointer<CChar>](./xpc_type_get_name%28_%29.md)
  Returns a string that describes an XPC object type.
- [func xpc_hash(xpc_object_t) -> Int](./xpc_hash%28_%29.md)
  Calculates a hash value for the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_get_type(_:))*