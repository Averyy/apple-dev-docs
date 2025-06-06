# xpc_fd_dup(_:)

**Framework**: Xpc  
**Kind**: func

Returns a file descriptor that is equivalent to the one that the specified file descriptor object boxes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_fd_dup(_ xfd: xpc_object_t) -> Int32
```

#### Return Value

A file descriptor that is equivalent to the one originally given to [`xpc_fd_create(_:)`](xpc_fd_create(_:).md). If the descriptor could not be created, -1 is returned.

#### Discussion

Multiple invocations of [`xpc_fd_dup(_:)`](xpc_fd_dup(_:).md) will not return the same file descriptor number, but they will return descriptors that are equivalent, as though they had been created by `dup(2)`.

The caller is responsible for calling `close(2)` on the returned descriptor.

## Parameters

- `xfd`: The file descriptor object which is to be examined.

## See Also

- [func xpc_fd_create(Int32) -> xpc_object_t?](xpc_fd_create(_:).md)
  Creates an XPC object that represents a POSIX file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_fd_dup(_:))*