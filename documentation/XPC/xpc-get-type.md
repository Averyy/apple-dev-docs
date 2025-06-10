# xpc_get_type(_:)

**Framework**: XPC  
**Kind**: func

Returns the type of an object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_get_type(_ object: xpc_object_t) -> xpc_type_t
```

#### Return Value

An opaque pointer describing the type of the object. This pointer is suitable for direct comparison to exported type constants with the equality operator.

## Parameters

- `object`: The object to examine.

## See Also

- [func xpc_type_get_name(xpc_type_t) -> UnsafePointer<CChar>](xpc_type_get_name(_:).md)
  Returns a string that describes an XPC object type.
- [func xpc_hash(xpc_object_t) -> Int](xpc_hash(_:).md)
  Calculates a hash value for the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_get_type(_:))*