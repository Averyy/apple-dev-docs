# ReadStreamsPipeTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.14+

## Declaration

```c
IOReturn (*ReadStreamsPipeTO)(void *self, UInt8 pipeRef, UInt32 streamID, void *buf, UInt32 *size, UInt32 noDataTimeout, UInt32 completionTimeout);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface942/2977239-readstreamspipeto)*