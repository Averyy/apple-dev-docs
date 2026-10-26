# ReadStreamsPipeAsyncTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.8+

## Declaration

```c
IOReturn (*ReadStreamsPipeAsyncTO)(void *self, UInt8 pipeRef, UInt32 streamID, void *buf, UInt32 size, UInt32 noDataTimeout, UInt32 completionTimeout, IOAsyncCallback1 callback, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface550/1559478-readstreamspipeasyncto)*