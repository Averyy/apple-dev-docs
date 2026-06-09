# unmapMemory(atOffset:size:completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Unmaps a chunk of host memory from the shared memory region.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func unmapMemory(atOffset offset: UInt64, size: UInt64) async throws
```

## Parameters

- `offset`: The offset from the start of the shared memory region where the memory should be unmapped.
- `size`: The size of the memory to be unmapped from the shared memory region.
- `completionHandler`: Block called after memory has been successfully unmapped or on error. The error parameter passed to the block is `nil` if the unmap operation is successful. The framework invokes the block on [`deviceQueue`](vzcustomvirtiodevice/devicequeue.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosharedmemoryregion/unmapmemory(atoffset:size:completionhandler:))*