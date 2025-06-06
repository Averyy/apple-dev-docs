# xpc_bool_create(_:)

**Framework**: Xpc  
**Kind**: func

Creates an XPC Boolean object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_bool_create(_ value: Bool) -> xpc_object_t
```

#### Return Value

A new Boolean object.

## Parameters

- `value`: The Boolean primitive value which is to be boxed.

## See Also

- [func xpc_bool_get_value(xpc_object_t) -> Bool](xpc_bool_get_value(_:).md)
  Returns the underlying Boolean value from the object.
- [var XPC_BOOL_TRUE: xpc_object_t](xpc_bool_true-swift.var.md)
  A constant that represents a Boolean value of true.
- [var XPC_BOOL_FALSE: xpc_object_t](xpc_bool_false-swift.var.md)
  A constant that represents a Boolean value of false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_bool_create(_:))*