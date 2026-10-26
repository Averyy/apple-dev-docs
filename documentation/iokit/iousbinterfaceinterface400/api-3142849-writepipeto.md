# WritePipeTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```c
IOReturn (*WritePipeTO)(void *self, UInt8 pipeRef, void *buf, UInt32 size, UInt32 noDataTimeout, UInt32 completionTimeout);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface400/3142849-writepipeto)*