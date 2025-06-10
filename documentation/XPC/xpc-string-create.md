# xpc_string_create(_:)

**Framework**: XPC  
**Kind**: func

Creates an XPC object that represents a null-terminated C-string.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_string_create(_ string: UnsafePointer<CChar>) -> xpc_object_t
```

#### Return Value

A new string object.

## Parameters

- `string`: The C-string which is to be boxed.

## See Also

- [func xpc_string_create_with_format_and_arguments(UnsafePointer<CChar>, CVaListPointer) -> xpc_object_t](xpc_string_create_with_format_and_arguments(_:_:).md)
  Creates an XPC object that represents a C-string that the specified format string and argument list pointer generate.
- [func xpc_string_get_length(xpc_object_t) -> Int](xpc_string_get_length(_:).md)
  Returns the length of the underlying string.
- [func xpc_string_get_string_ptr(xpc_object_t) -> UnsafePointer<CChar>?](xpc_string_get_string_ptr(_:).md)
  Returns a pointer to the internal storage of a string object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_string_create(_:))*