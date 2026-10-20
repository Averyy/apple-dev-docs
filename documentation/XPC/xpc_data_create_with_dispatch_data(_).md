# xpc_data_create_with_dispatch_data(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Creates an XPC object that represents a buffer of bytes that the specified GCD data object describes.

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
func xpc_data_create_with_dispatch_data(_ ddata: dispatch_data_t) -> xpc_object_t
```

```c
extern xpc_object_txpc_data_create_with_dispatch_data(dispatch_data_t ddata);
```

#### Return Value

A new data object.

#### Discussion

The object returned by this method will refer to the buffer returned by [`dispatch_data_create_map`](../Dispatch/dispatch_data_create_map.md). The point where XPC will make the call to [`dispatch_data_create_map`](../Dispatch/dispatch_data_create_map.md) is undefined.

## Parameters

- `ddata`: The GCD data object containing the bytes which are to be boxed. This object is retained by the data object.

## See Also

### Data objects
- [func xpc_data_create(UnsafeRawPointer?, Int) -> xpc_object_t](./xpc_data_create%28_,_%29.md)
  Creates an XPC object that represents a buffer of bytes.
- [func xpc_data_get_bytes(xpc_object_t, UnsafeMutableRawPointer, Int, Int) -> Int](./xpc_data_get_bytes%28_,_,_,_%29.md)
  Copies the bytes in a data object into the specified buffer.
- [func xpc_data_get_bytes_ptr(xpc_object_t) -> UnsafeRawPointer?](./xpc_data_get_bytes_ptr%28_%29.md)
  Returns a pointer to the internal storage of a data object.
- [func xpc_data_get_length(xpc_object_t) -> Int](./xpc_data_get_length%28_%29.md)
  Returns the length of the data that an XPC data object encapsulates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_data_create_with_dispatch_data(_:))*