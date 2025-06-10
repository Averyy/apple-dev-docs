# xpc_data_get_bytes_ptr(_:)

**Framework**: XPC  
**Kind**: func

Returns a pointer to the internal storage of a data object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_data_get_bytes_ptr(_ xdata: xpc_object_t) -> UnsafeRawPointer?
```

#### Return Value

A pointer to the underlying boxed data.

## Parameters

- `xdata`: The data object which is to be examined.

## See Also

- [func xpc_data_create(UnsafeRawPointer?, Int) -> xpc_object_t](xpc_data_create(_:_:).md)
  Creates an XPC object that represents a buffer of bytes.
- [func xpc_data_create_with_dispatch_data(dispatch_data_t) -> xpc_object_t](xpc_data_create_with_dispatch_data(_:).md)
  Creates an XPC object that represents a buffer of bytes that the specified GCD data object describes.
- [func xpc_data_get_bytes(xpc_object_t, UnsafeMutableRawPointer, Int, Int) -> Int](xpc_data_get_bytes(_:_:_:_:).md)
  Copies the bytes in a data object into the specified buffer.
- [func xpc_data_get_length(xpc_object_t) -> Int](xpc_data_get_length(_:).md)
  Returns the length of the data that an XPC data object encapsulates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_data_get_bytes_ptr(_:))*