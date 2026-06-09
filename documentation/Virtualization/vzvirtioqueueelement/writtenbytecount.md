# writtenByteCount

**Framework**: Virtualization  
**Kind**: property

The size of the write buffers memory exposed (in bytes) by the Virtio queue element that has already been written to.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var writtenByteCount: Int { get }
```

#### Discussion

This value increases as you write memory to the write buffers. This value is initially equal to 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/writtenbytecount)*