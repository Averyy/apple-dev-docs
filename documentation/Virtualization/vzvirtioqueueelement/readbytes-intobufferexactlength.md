# readBytes(intoBuffer:exactLength:)

**Framework**: Virtualization  
**Kind**: method

Reads the number of bytes you specify from the read buffers into the memory pointed to by the pointer to the buffer you provide.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func readBytes(intoBuffer buffer: UnsafeMutableRawPointer, exactLength: Int) throws
```

## Parameters

- `buffer`: Pointer to where the framework reads the read buffer’s memory to.
- `exactLength`: Number of bytes to read from the read buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/readbytes(intobuffer:exactlength:))*