# xpc_double_create(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Creates an XPC double object.

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
func xpc_double_create(_ value: Double) -> xpc_object_t
```

```c
extern xpc_object_txpc_double_create(double value);
```

## Return Value

A new floating point object.

## Parameters

- `value`: The floating point quantity which is to be boxed.

## See Also

### Number objects
- [func xpc_double_get_value(xpc_object_t) -> Double](./xpc_double_get_value%28_%29.md)
  Returns the underlying double-precision floating point value from an object.
- [func xpc_int64_create(Int64) -> xpc_object_t](./xpc_int64_create%28_%29.md)
  Creates an XPC signed integer object.
- [func xpc_int64_get_value(xpc_object_t) -> Int64](./xpc_int64_get_value%28_%29.md)
  Returns the underlying signed 64-bit integer value from an object.
- [func xpc_uint64_create(UInt64) -> xpc_object_t](./xpc_uint64_create%28_%29.md)
  Creates an XPC unsigned integer object.
- [func xpc_uint64_get_value(xpc_object_t) -> UInt64](./xpc_uint64_get_value%28_%29.md)
  Returns the underlying unsigned 64-bit integer value from an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_double_create(_:))*