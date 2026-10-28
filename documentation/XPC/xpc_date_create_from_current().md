# xpc_date_create_from_current()

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Creates an XPC date object that represents the current date.

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
func xpc_date_create_from_current() -> xpc_object_t
```

```c
extern xpc_object_txpc_date_create_from_current();
```

## Return Value

A new date object representing the current date.

## See Also

### Date objects
- [func xpc_date_create(Int64) -> xpc_object_t](./xpc_date_create%28_%29.md)
  Creates an XPC date object.
- [func xpc_date_get_value(xpc_object_t) -> Int64](./xpc_date_get_value%28_%29.md)
  Returns the underlying date interval from an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_date_create_from_current())*