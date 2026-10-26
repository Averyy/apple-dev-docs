# GetPipeProperties

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.9+

## Declaration

```c
IOReturn (*GetPipeProperties)(void *self, UInt8 pipeRef, UInt8 *direction, UInt8 *number, UInt8 *transferType, UInt16 *maxPacketSize, UInt8 *interval);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface650/1558827-getpipeproperties)*