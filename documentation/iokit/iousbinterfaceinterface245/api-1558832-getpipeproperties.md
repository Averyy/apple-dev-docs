# GetPipeProperties

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.4+

## Declaration

```c
IOReturn (*GetPipeProperties)(void *self, UInt8 pipeRef, UInt8 *direction, UInt8 *number, UInt8 *transferType, UInt16 *maxPacketSize, UInt8 *interval);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface245/1558832-getpipeproperties)*