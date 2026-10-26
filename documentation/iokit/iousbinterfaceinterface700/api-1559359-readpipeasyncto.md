# ReadPipeAsyncTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.10+

## Declaration

```c
IOReturn (*ReadPipeAsyncTO)(void *self, UInt8 pipeRef, void *buf, UInt32 size, UInt32 noDataTimeout, UInt32 completionTimeout, IOAsyncCallback1 callback, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface700/1559359-readpipeasyncto)*