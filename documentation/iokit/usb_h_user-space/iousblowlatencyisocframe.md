# IOUSBLowLatencyIsocFrame

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBLowLatencyIsocFrame {
   IOReturn frStatus;
   UInt16 frReqCount;
   UInt16 frActCount;
   AbsoluteTime frTimeStamp;
};
```

## Overview

Structure used to encode information about each isoc frame that is processed at hardware interrupt time (low latency).

## Topics

### Fields
- [frStatus](../iousblowlatencyisocframe/api-1425755-frstatus.md)
  Returns status associated with the frame.
- [frReqCount](../iousblowlatencyisocframe/api-1425652-frreqcount.md)
  Input specifiying how many bytes to read or write.
- [frActCount](../iousblowlatencyisocframe/api-1426008-fractcount.md)
  Actual # of bytes transferred.
- [frTimeStamp](../iousblowlatencyisocframe/api-1426222-frtimestamp.md)
  Time stamp that indicates time when frame was procesed.

## See Also

### Related Documentation
- [IOUSBLowLatencyIsocFrame](../../kernel/iousblowlatencyisocframe.md)
  A structure for encoding information about each low-latency isochronous frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousblowlatencyisocframe)*