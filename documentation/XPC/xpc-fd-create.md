# xpc_fd_create(_:)

**Framework**: Xpc  
**Kind**: func

Creates an XPC object that represents a POSIX file descriptor.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_fd_create(_ fd: Int32) -> xpc_object_t?
```

#### Return Value

A new file descriptor object. `NULL` if sufficient memory could not be allocated or if the given file descriptor was not valid.

#### Discussion

This method performs the equivalent of a `dup(2)` on the descriptor, so it is safe to call `close(2)` on the descriptor after boxing it with a file descriptor object.

> ❗ **Important**:  Pointer equality is the ONLY valid test for equality between two file descriptor objects. There is no reliable way to determine whether two file descriptors refer to the same inode with the same capabilities, so two file descriptor objects created from the same underlying file descriptor number will not compare equally with [`xpc_equal(_:_:)`](xpc_equal(_:_:).md). This is also true of a file descriptor object created using [`xpc_copy(_:)`](xpc_copy(_:).md) and the original.

 Pointer equality is the ONLY valid test for equality between two file descriptor objects. There is no reliable way to determine whether two file descriptors refer to the same inode with the same capabilities, so two file descriptor objects created from the same underlying file descriptor number will not compare equally with [`xpc_equal(_:_:)`](xpc_equal(_:_:).md). This is also true of a file descriptor object created using [`xpc_copy(_:)`](xpc_copy(_:).md) and the original.

This also implies that two collections containing file descriptor objects cannot be equal unless the exact same object was inserted into both.

## Parameters

- `fd`: The file descriptor which is to be boxed.

## See Also

- [func xpc_fd_dup(xpc_object_t) -> Int32](xpc_fd_dup(_:).md)
  Returns a file descriptor that is equivalent to the one that the specified file descriptor object boxes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_fd_create(_:))*