# EnqueueInputBuffer

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*EnqueueInputBuffer)(IOStreamRef stream, IOStreamBufferID bufferID, IOByteCount dataOffset, IOByteCount dataLength, IOByteCount controlOffset, IOByteCount controlLength);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreaminterface/1579745-enqueueinputbuffer)*