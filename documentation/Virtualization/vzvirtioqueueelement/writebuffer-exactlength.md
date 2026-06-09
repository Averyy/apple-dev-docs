# writeBuffer(_:exactLength:)

**Framework**: Virtualization  
**Kind**: method

Writes to the memory represented by the pointer to the buffer you provide to the write buffers.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func writeBuffer(_ buffer: UnsafeMutableRawPointer, exactLength: Int) throws
```

## Parameters

- `buffer`: A pointer to the memory containing the data to write to the write buffers.
- `exactLength`: The number of bytes the framework should write to the write buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/writebuffer(_:exactlength:))*