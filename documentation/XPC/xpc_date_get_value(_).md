# xpc_date_get_value(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Returns the underlying date interval from an object.

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
func xpc_date_get_value(_ xdate: xpc_object_t) -> Int64
```

```c
extern int64_t xpc_date_get_value(xpc_object_t xdate);
```

#### Return Value

The underlying date interval.

## Parameters

- `xdate`: The date object which is to be examined.

## See Also

### Date objects
- [func xpc_date_create(Int64) -> xpc_object_t](./xpc_date_create%28_%29.md)
  Creates an XPC date object.
- [func xpc_date_create_from_current() -> xpc_object_t](./xpc_date_create_from_current%28%29.md)
  Creates an XPC date object that represents the current date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_date_get_value(_:))*