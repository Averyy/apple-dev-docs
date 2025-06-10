# readBytes

**Framework**: Kernel  
**Kind**: instm

Copy data from the IODMACommand's buffer to the specified buffer.

## Declaration

```swift
UInt64 readBytes(
 UInt64offset,
 void *bytes,
 UInt64length);
```

#### Return_value

The number of bytes copied, zero will be returned if the specified offset is beyond the prepared length of the IODMACommand.

#### Overview

This method copies data from the IODMACommand's memory at the given offset, to the caller's buffer. The IODMACommand must be prepared, and the offset is relative to the prepared offset.

## Parameters

- `offset`: A byte offset into the IODMACommand's memory, relative to the prepared offset.
- `bytes`: The caller supplied buffer to copy the data to.
- `length`: The length of the data to copy.

## See Also

- [- readBytes](iodmacommand/1547724-readbytes.md)
  Copy data from the IODMACommand's buffer to the specified buffer.
- [writeBytes](iodmacommand/1811341-writebytes.md)
  Copy data to the IODMACommand's buffer from the specified buffer.
- [- writeBytes](iodmacommand/1547742-writebytes.md)
  Copy data to the IODMACommand's buffer from the specified buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1811301-readbytes)*