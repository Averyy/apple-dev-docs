# AsyncIOBundled_Impl

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.15+ - Deprecated in 10.15.4

## Declaration

```c
kern_return_t AsyncIOBundled_Impl(uint32_t ioTransferIndex, uint32_t ioTransferCount, uint32_t *ioTransferAcceptedCount, const unsigned int *dataBufferLengthArray, int dataBufferLengthArrayCount, OSAction *completion, uint32_t completionTimeoutMs);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostpipe/3294688-asynciobundled_impl)*