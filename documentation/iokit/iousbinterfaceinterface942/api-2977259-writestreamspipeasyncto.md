# WriteStreamsPipeAsyncTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.14+

## Declaration

```c
IOReturn (*WriteStreamsPipeAsyncTO)(void *self, UInt8 pipeRef, UInt32 streamID, void *buf, UInt32 size, UInt32 noDataTimeout, UInt32 completionTimeout, IOAsyncCallback1 callback, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface942/2977259-writestreamspipeasyncto)*