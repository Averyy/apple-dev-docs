# IOFramebufferShared.h User-Space

**Framework**: IOKit  
**Role**: API Collection

## Overview

The IOFramebufferShared.h header contains definitions of objects and types shared between a kernel level IOFrameBuffer service and a non-kernel window server. In macOS this structure is used by the CoreGraphics server and IOGraphics Family, and is not available to other clients. IOFramebuffer subclasses and IOFramebuffer clients within the kernel should also not rely on this structure definition and constants. It is public only for use on Darwin based window servers. Cursor and window server state data is exchanged by kernel and non-kernel tasks through a slice of shared memory containing a StdFBShmem_t structure.

For a non-kernel task to get access to this slice of shared memory, a connection to an IOFramebuffer service must be made. A connection is made with the IOServiceOpen() function described in IOKitLib.h. A connection type of kIOFBServerConnectType or kIOFBSharedConnectType (for read-only access) should be specified. An io_connect_t handle is returned by IOServiceOpen(). This handle must be passed to IOFBCreateSharedCursor() to create the slice of shared memory. Then IOConnectMapMemory() may be called with a memory type of kIOFBCursorMemory to map the shared memory into the non-kernel task.

### Included Headers

- <IOKit/hidsystem/IOHIDTypes.h>
- <IOKit/graphics/IOGraphicsTypes.h>
- <libkern/OSAtomic.h>

## Topics

### Data Types
- [bm12Cursor](./bm12cursor.md)
  Cursor image for 1-bit cursor.
- [bm18Cursor](./bm18cursor.md)
  Cursor image for 8-bit cursor.
- [bm34Cursor](./bm34cursor.md)
  Cursor image for 15-bit cursor.
- [bm38Cursor](./bm38cursor.md)
  Cursor image for 24-bit cursor.
- [StdFBShmem_t](./stdfbshmem_t.md)
### Constants
- [Defines](./ioframebuffershared_h_user-space/defines.md)
- [CursorParameters](./api-1589167-cursorparameters.md)
- [FramebufferConstants](./ioframebuffershared_h_user-space/framebufferconstants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioframebuffershared_h_user-space)*