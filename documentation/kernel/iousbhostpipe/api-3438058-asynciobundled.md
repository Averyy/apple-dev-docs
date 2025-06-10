# AsyncIOBundled

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15+ - Deprecated in 10.15.4

## Declaration

```swift
kern_return_t AsyncIOBundled(uint32_t ioTransferIndex, uint32_t ioTransferCount, uint32_t *ioTransferAcceptedCount, const unsigned int *dataBufferLengthArray, int dataBufferLengthArrayCount, OSAction *completion, uint32_t completionTimeoutMs, OSDispatchMethod supermethod);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostpipe/3438058-asynciobundled)*