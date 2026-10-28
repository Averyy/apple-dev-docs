# XPC_BOOL_FALSE

**Framework**: XPC  
**Kind**: macro  
**Role**: Macro

A constant that represents a Boolean value of false.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define XPC_BOOL_FALSE
```

## Discussion

You may compare a Boolean object against this constant to determine its value.

## See Also

### Boolean objects
- [func xpc_bool_create(Bool) -> xpc_object_t](./xpc_bool_create%28_%29.md)
  Creates an XPC Boolean object.
- [func xpc_bool_get_value(xpc_object_t) -> Bool](./xpc_bool_get_value%28_%29.md)
  Returns the underlying Boolean value from the object.
- [XPC_BOOL_TRUE](./xpc_bool_true-c.macro.md)
  A constant that represents a Boolean value of true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_bool_false-c.macro)*