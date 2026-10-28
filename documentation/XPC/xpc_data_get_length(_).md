# xpc_data_get_length(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Returns the length of the data that an XPC data object encapsulates.

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
func xpc_data_get_length(_ xdata: xpc_object_t) -> Int
```

```c
extern size_t xpc_data_get_length(xpc_object_t xdata);
```

## Return Value

The length of the underlying boxed data.

## Parameters

- `xdata`: The data object which is to be examined.

## See Also

### Data objects
- [func xpc_data_create(UnsafeRawPointer?, Int) -> xpc_object_t](./xpc_data_create%28_,_%29.md)
  Creates an XPC object that represents a buffer of bytes.
- [func xpc_data_create_with_dispatch_data(dispatch_data_t) -> xpc_object_t](./xpc_data_create_with_dispatch_data%28_%29.md)
  Creates an XPC object that represents a buffer of bytes that the specified GCD data object describes.
- [func xpc_data_get_bytes(xpc_object_t, UnsafeMutableRawPointer, Int, Int) -> Int](./xpc_data_get_bytes%28_,_,_,_%29.md)
  Copies the bytes in a data object into the specified buffer.
- [func xpc_data_get_bytes_ptr(xpc_object_t) -> UnsafeRawPointer?](./xpc_data_get_bytes_ptr%28_%29.md)
  Returns a pointer to the internal storage of a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_data_get_length(_:))*