# ReadStreamsPipeTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.9+

## Declaration

```c
IOReturn (*ReadStreamsPipeTO)(void *self, UInt8 pipeRef, UInt32 streamID, void *buf, UInt32 *size, UInt32 noDataTimeout, UInt32 completionTimeout);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface650/1558940-readstreamspipeto)*