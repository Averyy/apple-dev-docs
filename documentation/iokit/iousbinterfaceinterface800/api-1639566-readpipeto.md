# ReadPipeTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.12+

## Declaration

```c
IOReturn (*ReadPipeTO)(void *self, UInt8 pipeRef, void *buf, UInt32 *size, UInt32 noDataTimeout, UInt32 completionTimeout);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface800/1639566-readpipeto)*