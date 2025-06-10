# xpc_uint64_get_value(_:)

**Framework**: XPC  
**Kind**: func

Returns the underlying unsigned 64-bit integer value from an object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_uint64_get_value(_ xuint: xpc_object_t) -> UInt64
```

#### Return Value

The underlying unsigned integer value.

## Parameters

- `xuint`: The unsigned integer object which is to be examined.

## See Also

- [func xpc_double_create(Double) -> xpc_object_t](xpc_double_create(_:).md)
  Creates an XPC double object.
- [func xpc_double_get_value(xpc_object_t) -> Double](xpc_double_get_value(_:).md)
  Returns the underlying double-precision floating point value from an object.
- [func xpc_int64_create(Int64) -> xpc_object_t](xpc_int64_create(_:).md)
  Creates an XPC signed integer object.
- [func xpc_int64_get_value(xpc_object_t) -> Int64](xpc_int64_get_value(_:).md)
  Returns the underlying signed 64-bit integer value from an object.
- [func xpc_uint64_create(UInt64) -> xpc_object_t](xpc_uint64_create(_:).md)
  Creates an XPC unsigned integer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_uint64_get_value(_:))*