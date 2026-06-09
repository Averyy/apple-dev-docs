# writeBuffersAvailableByteCount

**Framework**: Virtualization  
**Kind**: property

The size of the write buffers memory (in bytes) exposed by the Virtio queue element that’s currently available for writing.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var writeBuffersAvailableByteCount: Int { get }
```

#### Discussion

This value is initially equal to `writeBuffersByteCount`. This value decreases as you write memory to the write buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/writebuffersavailablebytecount)*