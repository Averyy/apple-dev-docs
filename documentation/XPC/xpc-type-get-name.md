# xpc_type_get_name(_:)

**Framework**: XPC  
**Kind**: func

Returns a string that describes an XPC object type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
func xpc_type_get_name(_ type: xpc_type_t) -> UnsafePointer<CChar>
```

#### Return Value

A string describing the type of an object, like `"string"` or `"int64"`. This string should not be freed or modified.

## Parameters

- `type`: The type to describe.

## See Also

- [func xpc_get_type(xpc_object_t) -> xpc_type_t](xpc_get_type(_:).md)
  Returns the type of an object.
- [func xpc_hash(xpc_object_t) -> Int](xpc_hash(_:).md)
  Calculates a hash value for the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_type_get_name(_:))*