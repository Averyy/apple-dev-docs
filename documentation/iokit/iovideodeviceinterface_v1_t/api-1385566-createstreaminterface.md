# CreateStreamInterface

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
IOReturn (*CreateStreamInterface)(IOVideoDeviceRef device, CFDictionaryRef streamDictionary, UInt32 streamIndex, bool isInput, IOStreamRef *streamRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iovideodeviceinterface_v1_t/1385566-createstreaminterface)*