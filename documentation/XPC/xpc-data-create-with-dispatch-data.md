# xpc_data_create_with_dispatch_data(_:)

**Framework**: XPC  
**Kind**: func

Creates an XPC object that represents a buffer of bytes that the specified GCD data object describes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_data_create_with_dispatch_data(_ ddata: dispatch_data_t) -> xpc_object_t
```

#### Return Value

A new data object.

#### Discussion

The object returned by this method will refer to the buffer returned by [`dispatch_data_create_map`](https://developer.apple.com/documentation/Dispatch/dispatch_data_create_map). The point where XPC will make the call to [`dispatch_data_create_map`](https://developer.apple.com/documentation/Dispatch/dispatch_data_create_map) is undefined.

## Parameters

- `ddata`: The GCD data object containing the bytes which are to be boxed. This object is retained by the data object.

## See Also

- [func xpc_data_create(UnsafeRawPointer?, Int) -> xpc_object_t](xpc_data_create(_:_:).md)
  Creates an XPC object that represents a buffer of bytes.
- [func xpc_data_get_bytes(xpc_object_t, UnsafeMutableRawPointer, Int, Int) -> Int](xpc_data_get_bytes(_:_:_:_:).md)
  Copies the bytes in a data object into the specified buffer.
- [func xpc_data_get_bytes_ptr(xpc_object_t) -> UnsafeRawPointer?](xpc_data_get_bytes_ptr(_:).md)
  Returns a pointer to the internal storage of a data object.
- [func xpc_data_get_length(xpc_object_t) -> Int](xpc_data_get_length(_:).md)
  Returns the length of the data that an XPC data object encapsulates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_data_create_with_dispatch_data(_:))*