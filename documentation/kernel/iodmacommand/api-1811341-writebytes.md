# writeBytes

**Framework**: Kernel  
**Kind**: instm

Copy data to the IODMACommand's buffer from the specified buffer.

## Declaration

```c
UInt64 writeBytes(
 UInt64offset,
 const void *bytes,
 UInt64length);
```

## Return Value

The number of bytes copied, zero will be returned if the specified offset is beyond the prepared length of the IODMACommand.

## Overview

This method copies data to the IODMACommand's memory at the given offset, from the caller's buffer. The IODMACommand must be prepared, and the offset is relative to the prepared offset.

## Parameters

- `offset`: A byte offset into the IODMACommand's memory, relative to the prepared offset.
- `bytes`: The caller supplied buffer to copy the data from.
- `length`: The length of the data to copy.

## See Also

### Transferring Data
- [readBytes](./api-1811301-readbytes.md)
  Copy data from the IODMACommand's buffer to the specified buffer.
- [- readBytes](./api-1547724-readbytes.md)
  Copy data from the IODMACommand's buffer to the specified buffer.
- [- writeBytes](./api-1547742-writebytes.md)
  Copy data to the IODMACommand's buffer from the specified buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1811341-writebytes)*