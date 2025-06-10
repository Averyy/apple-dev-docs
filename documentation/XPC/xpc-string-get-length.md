# xpc_string_get_length(_:)

**Framework**: XPC  
**Kind**: func

Returns the length of the underlying string.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_string_get_length(_ xstring: xpc_object_t) -> Int
```

#### Return Value

The length of the underlying string, not including the `NULL`-terminator.

## Parameters

- `xstring`: The string object which is to be examined.

## See Also

- [func xpc_string_create(UnsafePointer<CChar>) -> xpc_object_t](xpc_string_create(_:).md)
  Creates an XPC object that represents a null-terminated C-string.
- [func xpc_string_create_with_format_and_arguments(UnsafePointer<CChar>, CVaListPointer) -> xpc_object_t](xpc_string_create_with_format_and_arguments(_:_:).md)
  Creates an XPC object that represents a C-string that the specified format string and argument list pointer generate.
- [func xpc_string_get_string_ptr(xpc_object_t) -> UnsafePointer<CChar>?](xpc_string_get_string_ptr(_:).md)
  Returns a pointer to the internal storage of a string object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_string_get_length(_:))*