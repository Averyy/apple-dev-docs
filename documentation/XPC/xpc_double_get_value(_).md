# xpc_double_get_value(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Returns the underlying double-precision floating point value from an object.

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
func xpc_double_get_value(_ xdouble: xpc_object_t) -> Double
```

```c
extern double xpc_double_get_value(xpc_object_t xdouble);
```

#### Return Value

The underlying floating point value.

## Parameters

- `xdouble`: The floating point object which is to be examined.

## See Also

### Number objects
- [func xpc_double_create(Double) -> xpc_object_t](./xpc_double_create%28_%29.md)
  Creates an XPC double object.
- [func xpc_int64_create(Int64) -> xpc_object_t](./xpc_int64_create%28_%29.md)
  Creates an XPC signed integer object.
- [func xpc_int64_get_value(xpc_object_t) -> Int64](./xpc_int64_get_value%28_%29.md)
  Returns the underlying signed 64-bit integer value from an object.
- [func xpc_uint64_create(UInt64) -> xpc_object_t](./xpc_uint64_create%28_%29.md)
  Creates an XPC unsigned integer object.
- [func xpc_uint64_get_value(xpc_object_t) -> UInt64](./xpc_uint64_get_value%28_%29.md)
  Returns the underlying unsigned 64-bit integer value from an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_double_get_value(_:))*