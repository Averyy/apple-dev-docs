# xpc_int64_create(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Creates an XPC signed integer object.

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
func xpc_int64_create(_ value: Int64) -> xpc_object_t
```

```c
extern xpc_object_txpc_int64_create(int64_t value);
```

#### Return Value

A new signed integer object.

## Parameters

- `value`: The signed integer value which is to be boxed.

## See Also

### Number objects
- [func xpc_double_create(Double) -> xpc_object_t](./xpc_double_create%28_%29.md)
  Creates an XPC double object.
- [func xpc_double_get_value(xpc_object_t) -> Double](./xpc_double_get_value%28_%29.md)
  Returns the underlying double-precision floating point value from an object.
- [func xpc_int64_get_value(xpc_object_t) -> Int64](./xpc_int64_get_value%28_%29.md)
  Returns the underlying signed 64-bit integer value from an object.
- [func xpc_uint64_create(UInt64) -> xpc_object_t](./xpc_uint64_create%28_%29.md)
  Creates an XPC unsigned integer object.
- [func xpc_uint64_get_value(xpc_object_t) -> UInt64](./xpc_uint64_get_value%28_%29.md)
  Returns the underlying unsigned 64-bit integer value from an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_int64_create(_:))*