# xpc_string_create_with_format_and_arguments(_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Creates an XPC object that represents a C-string that the specified format string and argument list pointer generate.

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
func xpc_string_create_with_format_and_arguments(_ fmt: UnsafePointer<CChar>, _ ap: CVaListPointer) -> xpc_object_t
```

```c
extern xpc_object_txpc_string_create_with_format_and_arguments(const char *fmt, va_list ap);
```

#### Return Value

A new string object.

## Parameters

- `fmt`: The `printf(3)`-style format string from which to construct the final C-string to be boxed.
- `ap`: A pointer to the arguments which correspond to those specified in the format string.

## See Also

### String objects
- [func xpc_string_create(UnsafePointer<CChar>) -> xpc_object_t](./xpc_string_create%28_%29.md)
  Creates an XPC object that represents a null-terminated C-string.
- [func xpc_string_get_length(xpc_object_t) -> Int](./xpc_string_get_length%28_%29.md)
  Returns the length of the underlying string.
- [func xpc_string_get_string_ptr(xpc_object_t) -> UnsafePointer<CChar>?](./xpc_string_get_string_ptr%28_%29.md)
  Returns a pointer to the internal storage of a string object.
- [xpc_string_create_with_format](./xpc_string_create_with_format.md)
  Creates an XPC object that represents a C-string that the specified format string and arguments generate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_string_create_with_format_and_arguments(_:_:))*