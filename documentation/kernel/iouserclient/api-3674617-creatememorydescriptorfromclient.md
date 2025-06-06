# CreateMemoryDescriptorFromClient

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 11.0+

## Declaration

```swift
kern_return_t CreateMemoryDescriptorFromClient(uint64_t memoryDescriptorCreateOptions, uint32_t segmentsCount, const IOAddressSegment *segments, IOMemoryDescriptor **memory, OSDispatchMethod supermethod);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iouserclient/3674617-creatememorydescriptorfromclient)*