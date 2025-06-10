# GetStateBits

**Framework**: Kernel  
**Kind**: enum

The bits in the value returned by getState().

## Declaration

```swift
enum {
   kStateRunning = 0x1,
   kStateOutputStalled = 0x2,
   kStateOutputActive = 0x4,
   kStateOutputServiceMask = 0xff00
};
```

## Topics

### Constants
- [kStateRunning](iobasicoutputqueue/getstatebits/kstaterunning.md)
- [kStateStalled](iobasicoutputqueue/getstatebits/kstatestalled.md)
- [kStateActive](iobasicoutputqueue/getstatebits/kstateactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobasicoutputqueue/getstatebits)*