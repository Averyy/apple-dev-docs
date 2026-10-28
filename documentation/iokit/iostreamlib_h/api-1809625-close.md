# Close

**Framework**: IOKit  
**Kind**: func

Closes an IOStream.

## Declaration

```c
IOReturn ( *Close)(
   IOStreamRef stream );
```

## Return Value

Returns kIOReturnSuccess if the stream was successfully closed and the buffers unmapped.

## Overview

Calling Close umaps all shared memory for the stream and frees all user resources used by the stream.

## Parameters

- `stream`: The IOStreamRef of the stream to close.

## See Also

### Opening and closing streams
- [Open](./api-1809697-open.md)
  Open an IOStream from user space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1809625-close)*