# FramebufferConstants

**Framework**: IOKit  
**Kind**: enum

## Declaration

```c
enum {
   // version for IOFBCreateSharedCursor
   kIOFBShmemVersionMask = 0x000000ff,
   kIOFBTenPtOneShmemVersion = 2,
   kIOFBTenPtTwoShmemVersion = 3,
   kIOFBCurrentShmemVersion = 2,
   // number of frames in animating cursor (if > kIOFBTenPtTwoShmemVersion)
   kIOFBShmemCursorNumFramesMask = 0x00ff0000,
   kIOFBShmemCursorNumFramesShift = 16,
   // memory types for IOConnectMapMemory.
   kIOFBCursorMemory = 100
};
```

## Topics

### Constants
- [kIOFBCurrentShmemVersion](../api-1589180-anonymous/kiofbcurrentshmemversion.md)
- [kIOFBCursorMemory](../api-1589180-anonymous/kiofbcursormemory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioframebuffershared_h_user-space/framebufferconstants)*