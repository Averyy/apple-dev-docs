# GetStateBits

**Framework**: Kernel  
**Kind**: enum

The bits in the value returned by getState().

## Declaration

```c
enum {
   kStateRunning = 0x1,
   kStateOutputStalled = 0x2,
   kStateOutputActive = 0x4,
   kStateOutputServiceMask = 0xff00
};
```

## Topics

### Constants
- [kStateRunning](./getstatebits/kstaterunning.md)
- [kStateStalled](./getstatebits/kstatestalled.md)
- [kStateActive](./getstatebits/kstateactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobasicoutputqueue/getstatebits)*