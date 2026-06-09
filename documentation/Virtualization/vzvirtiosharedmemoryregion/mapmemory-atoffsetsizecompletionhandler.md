# mapMemory(_:atOffset:size:completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Maps a chunk of host memory into the shared memory region.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func mapMemory(_ memory: UnsafeMutableRawPointer, atOffset offset: UInt64, size: UInt64) async throws
```

## Parameters

- `memory`: A pointer to host memory to map into the shared memory region.
- `offset`: The offset from the start of the shared memory region where the memory should map to.
- `size`: The size of the memory to map into the shared memory region.
- `completionHandler`: A block the framework calls after successfully mapping the memory, or on an error. The error parameter passed to the block is `nil` if the map operation is successful. The framework invokes the block on [`deviceQueue`](vzcustomvirtiodevice/devicequeue.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosharedmemoryregion/mapmemory(_:atoffset:size:completionhandler:))*