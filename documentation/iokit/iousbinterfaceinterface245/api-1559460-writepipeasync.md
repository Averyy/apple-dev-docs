# WritePipeAsync

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.4+

## Declaration

```c
IOReturn (*WritePipeAsync)(void *self, UInt8 pipeRef, void *buf, UInt32 size, IOAsyncCallback1 callback, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface245/1559460-writepipeasync)*