# xpc_date_create(_:)

**Framework**: XPC  
**Kind**: func

Creates an XPC date object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_date_create(_ interval: Int64) -> xpc_object_t
```

#### Return Value

A new date object.

## Parameters

- `interval`: The date interval which is to be boxed. Negative values indicate the number of nanoseconds before the epoch. Positive values indicate the number of nanoseconds after the epoch.

## See Also

- [func xpc_date_create_from_current() -> xpc_object_t](xpc_date_create_from_current().md)
  Creates an XPC date object that represents the current date.
- [func xpc_date_get_value(xpc_object_t) -> Int64](xpc_date_get_value(_:).md)
  Returns the underlying date interval from an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_date_create(_:))*