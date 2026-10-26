# USBLowLatencyBufferType

**Framework**: IOKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
typedef enum USBLowLatencyBufferType : unsigned int {
    ...
} USBLowLatencyBufferType;
```

#### Overview

Used to specify what kind of buffer to create when calling LowLatencyCreateBuffer().

## Topics

### Constants
- [kUSBLowLatencyWriteBuffer](./usblowlatencybuffertype/kusblowlatencywritebuffer.md)
- [kUSBLowLatencyReadBuffer](./usblowlatencybuffertype/kusblowlatencyreadbuffer.md)
- [kUSBLowLatencyFrameListBuffer](./usblowlatencybuffertype/kusblowlatencyframelistbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usblowlatencybuffertype)*