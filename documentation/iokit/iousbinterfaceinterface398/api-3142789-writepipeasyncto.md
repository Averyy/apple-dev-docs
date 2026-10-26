# WritePipeAsyncTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```c
IOReturn (*WritePipeAsyncTO)(void *self, UInt8 pipeRef, void *buf, UInt32 size, UInt32 noDataTimeout, UInt32 completionTimeout, IOAsyncCallback1 callback, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface398/3142789-writepipeasyncto)*