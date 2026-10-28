# xpc_bool_get_value(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Returns the underlying Boolean value from the object.

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
func xpc_bool_get_value(_ xbool: xpc_object_t) -> Bool
```

```c
extern bool xpc_bool_get_value(xpc_object_t xbool);
```

## Return Value

The underlying Boolean value.

## Parameters

- `xbool`: The Boolean object which is to be examined.

## See Also

### Boolean objects
- [func xpc_bool_create(Bool) -> xpc_object_t](./xpc_bool_create%28_%29.md)
  Creates an XPC Boolean object.
- [var XPC_BOOL_TRUE: xpc_object_t](./xpc_bool_true-swift.var.md)
  A constant that represents a Boolean value of true.
- [var XPC_BOOL_FALSE: xpc_object_t](./xpc_bool_false-swift.var.md)
  A constant that represents a Boolean value of false.
- [XPC_BOOL_TRUE](./xpc_bool_true-c.macro.md)
  A constant that represents a Boolean value of true.
- [XPC_BOOL_FALSE](./xpc_bool_false-c.macro.md)
  A constant that represents a Boolean value of false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_bool_get_value(_:))*