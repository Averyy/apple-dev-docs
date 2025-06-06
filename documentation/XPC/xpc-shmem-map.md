# xpc_shmem_map(_:_:)

**Framework**: Xpc  
**Kind**: func

Maps the region that the XPC shared memory object boxes into the caller’s address space.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_shmem_map(_ xshmem: xpc_object_t, _ region: UnsafeMutablePointer<UnsafeMutableRawPointer?>) -> Int
```

#### Return Value

The length of the region that was mapped. If the mapping failed, 0 is returned.

#### Discussion

The resulting region must be disposed of with `munmap(2)`.

It is the responsibility of the caller to manage protections on the new region accordingly.

## Parameters

- `xshmem`: The shared memory object to be examined.
- `region`: On return, this will point to the region at which the shared memory was mapped.

## See Also

- [func xpc_shmem_create(UnsafeMutableRawPointer, Int) -> xpc_object_t](xpc_shmem_create(_:_:).md)
  Creates an XPC object that represents the specified shared memory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_shmem_map(_:_:))*