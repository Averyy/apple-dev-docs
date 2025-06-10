# XPC_BOOL_TRUE

**Framework**: XPC  
**Kind**: var

A constant that represents a Boolean value of true.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
var XPC_BOOL_TRUE: xpc_object_t { get }
```

#### Discussion

You may compare a Boolean object against this constant to determine its value.

## See Also

- [func xpc_bool_create(Bool) -> xpc_object_t](xpc_bool_create(_:).md)
  Creates an XPC Boolean object.
- [func xpc_bool_get_value(xpc_object_t) -> Bool](xpc_bool_get_value(_:).md)
  Returns the underlying Boolean value from the object.
- [var XPC_BOOL_FALSE: xpc_object_t](xpc_bool_false-swift.var.md)
  A constant that represents a Boolean value of false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_bool_true-swift.var)*