# writeBytes

**Framework**: Kernel  
**Kind**: instm

Copy data to the IODMACommand's buffer from the specified buffer.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
UInt64 writeBytes(UInt64 offset, const void *bytes, UInt64 length);
```

#### Return_value

The number of bytes copied, zero will be returned if the specified offset is beyond the prepared length of the IODMACommand.

#### Discussion

This method copies data to the IODMACommand's memory at the given offset, from the caller's buffer. The IODMACommand must be prepared, and the offset is relative to the prepared offset.

## Parameters

- `offset`: A byte offset into the IODMACommand's memory, relative to the prepared offset.
- `bytes`: The caller supplied buffer to copy the data from.
- `length`: The length of the data to copy.

## See Also

- [readBytes](iodmacommand/1811301-readbytes.md)
  Copy data from the IODMACommand's buffer to the specified buffer.
- [- readBytes](iodmacommand/1547724-readbytes.md)
  Copy data from the IODMACommand's buffer to the specified buffer.
- [writeBytes](iodmacommand/1811341-writebytes.md)
  Copy data to the IODMACommand's buffer from the specified buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1547742-writebytes)*