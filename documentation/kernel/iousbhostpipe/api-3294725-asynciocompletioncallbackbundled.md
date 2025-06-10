# asyncIOCompletionCallbackBundled

**Framework**: Kernel  
**Kind**: clm

**Availability**:
- macOS 10.15+ - Deprecated in 10.15.4

## Declaration

```swift
static void asyncIOCompletionCallbackBundled(void *owner, uint32_t ioCompletionCount, IOMemoryDescriptor **dataBufferArray, void **parameterArray, IOReturn *statusArray, uint32_t *actualByteCountArray);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostpipe/3294725-asynciocompletioncallbackbundled)*