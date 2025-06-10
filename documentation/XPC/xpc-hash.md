# xpc_hash(_:)

**Framework**: XPC  
**Kind**: func

Calculates a hash value for the specified object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_hash(_ object: xpc_object_t) -> Int
```

#### Return Value

The calculated hash value.

#### Discussion

Note that the computed hash values for any particular type and value of an object can change from across releases and platforms and should not be assumed to be constant across all time and space or stored persistently.

## Parameters

- `object`: The object for which to calculate a hash value. This value may be modded with a table size for insertion into a dictionary-like data structure.

## See Also

- [func xpc_get_type(xpc_object_t) -> xpc_type_t](xpc_get_type(_:).md)
  Returns the type of an object.
- [func xpc_type_get_name(xpc_type_t) -> UnsafePointer<CChar>](xpc_type_get_name(_:).md)
  Returns a string that describes an XPC object type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_hash(_:))*