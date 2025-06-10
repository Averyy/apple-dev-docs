# readBytes

**Framework**: Kernel  
**Kind**: instm

Copy data from the memory descriptor's buffer to the specified buffer.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOByteCount readBytes(IOByteCount offset, void *bytes, IOByteCount withLength);
```

#### Return_value

The number of bytes copied, zero will be returned if the specified offset is beyond the length of the descriptor. Development/debug kernel builds will assert if the offset is beyond the length of the descriptor.

#### Discussion

This method copies data from the memory descriptor's memory at the given offset, to the caller's buffer. The memory descriptor MUST have the kIODirectionOut direcction bit set and be prepared. kIODirectionOut means that this memory descriptor will be output to an external device, so readBytes is used to get memory into a local buffer for a PIO transfer to the device.

## Parameters

- `offset`: A byte offset into the memory descriptor's memory.
- `bytes`: The caller supplied buffer to copy the data to.
- `withLength`: The length of the data to copy.

## See Also

- [readBytes](iomemorydescriptor/1812854-readbytes.md)
  Copy data from the memory descriptor's buffer to the specified buffer.
- [writeBytes](iomemorydescriptor/1812910-writebytes.md)
  Copy data to the memory descriptor's buffer from the specified buffer.
- [- writeBytes](iomemorydescriptor/1442038-writebytes.md)
  Copy data to the memory descriptor's buffer from the specified buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1441823-readbytes)*