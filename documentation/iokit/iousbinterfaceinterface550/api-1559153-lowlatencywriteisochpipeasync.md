# LowLatencyWriteIsochPipeAsync

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.8+

## Declaration

```c
IOReturn (*LowLatencyWriteIsochPipeAsync)(void *self, UInt8 pipeRef, void *buf, UInt64 frameStart, UInt32 numFrames, UInt32 updateFrequency, IOUSBLowLatencyIsocFrame *frameList, IOAsyncCallback1 callback, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface550/1559153-lowlatencywriteisochpipeasync)*