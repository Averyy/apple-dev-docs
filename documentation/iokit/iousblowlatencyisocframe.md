# IOUSBLowLatencyIsocFrame

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
typedef struct IOUSBLowLatencyIsocFrame {
    ...
} IOUSBLowLatencyIsocFrame;
```

## Overview

Structure used to encode information about each isoc frame that is processed at hardware interrupt time (low latency).

## Topics

### Instance Properties
- [frActCount](./iousblowlatencyisocframe/api-1426008-fractcount.md)
  Actual # of bytes transferred.
- [frReqCount](./iousblowlatencyisocframe/api-1425652-frreqcount.md)
  Input specifiying how many bytes to read or write.
- [frStatus](./iousblowlatencyisocframe/api-1425755-frstatus.md)
  Returns status associated with the frame.
- [frTimeStamp](./iousblowlatencyisocframe/api-1426222-frtimestamp.md)
  Time stamp that indicates time when frame was procesed.

## See Also

### Related Documentation
- [IOUSBLowLatencyIsocFrame](./usb_h_user-space/iousblowlatencyisocframe.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousblowlatencyisocframe)*