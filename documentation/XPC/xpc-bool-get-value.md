# xpc_bool_get_value(_:)

**Framework**: XPC  
**Kind**: func

Returns the underlying Boolean value from the object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_bool_get_value(_ xbool: xpc_object_t) -> Bool
```

#### Return Value

The underlying Boolean value.

## Parameters

- `xbool`: The Boolean object which is to be examined.

## See Also

- [func xpc_bool_create(Bool) -> xpc_object_t](xpc_bool_create(_:).md)
  Creates an XPC Boolean object.
- [var XPC_BOOL_TRUE: xpc_object_t](xpc_bool_true-swift.var.md)
  A constant that represents a Boolean value of true.
- [var XPC_BOOL_FALSE: xpc_object_t](xpc_bool_false-swift.var.md)
  A constant that represents a Boolean value of false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_bool_get_value(_:))*