# GetBufferInfo

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*GetBufferInfo)(IOStreamRef stream, IOStreamBufferID bufferID, void **dataBufferAddressOut, IOByteCount *dataBufferSizeOut, void **controlBufferAddressOut, IOByteCount *controlBufferSizeOut);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreaminterface/1579738-getbufferinfo)*