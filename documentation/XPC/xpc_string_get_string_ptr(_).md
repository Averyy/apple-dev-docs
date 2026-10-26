# xpc_string_get_string_ptr(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Returns a pointer to the internal storage of a string object.

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
func xpc_string_get_string_ptr(_ xstring: xpc_object_t) -> UnsafePointer<CChar>?
```

```c
extern const char *xpc_string_get_string_ptr(xpc_object_t xstring);
```

#### Return Value

A pointer to the string object’s internal storage.

## Parameters

- `xstring`: The string object which is to be examined.

## See Also

### String objects
- [func xpc_string_create(UnsafePointer<CChar>) -> xpc_object_t](./xpc_string_create%28_%29.md)
  Creates an XPC object that represents a null-terminated C-string.
- [func xpc_string_create_with_format_and_arguments(UnsafePointer<CChar>, CVaListPointer) -> xpc_object_t](./xpc_string_create_with_format_and_arguments%28_,_%29.md)
  Creates an XPC object that represents a C-string that the specified format string and argument list pointer generate.
- [func xpc_string_get_length(xpc_object_t) -> Int](./xpc_string_get_length%28_%29.md)
  Returns the length of the underlying string.
- [xpc_string_create_with_format](./xpc_string_create_with_format.md)
  Creates an XPC object that represents a C-string that the specified format string and arguments generate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_string_get_string_ptr(_:))*