# xpc_shmem_create(_:_:)

**Framework**: XPC  
**Kind**: func

Creates an XPC object that represents the specified shared memory region.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_shmem_create(_ region: UnsafeMutableRawPointer, _ length: Int) -> xpc_object_t
```

#### Return Value

A new shared memory object.

#### Discussion

This API is NOT for making a private region of memory shareable. It is to allow for already-shareable regions of memory to be boxed in an XPC object. Do not pass a region allocated with `malloc(3)` or friends to this API.

## Parameters

- `region`: A pointer to a region of shared memory, created through a call to mmap(2) with the MAP_SHARED flag, which is to be boxed.
- `length`: The length of the region.

## See Also

- [func xpc_shmem_map(xpc_object_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>) -> Int](xpc_shmem_map(_:_:).md)
  Maps the region that the XPC shared memory object boxes into the caller’s address space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_shmem_create(_:_:))*