# ReadIsochPipeAsync

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.12+

## Declaration

```c
IOReturn (*ReadIsochPipeAsync)(void *self, UInt8 pipeRef, void *buf, UInt64 frameStart, UInt32 numFrames, IOUSBIsocFrame *frameList, IOAsyncCallback1 callback, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface800/1639603-readisochpipeasync)*