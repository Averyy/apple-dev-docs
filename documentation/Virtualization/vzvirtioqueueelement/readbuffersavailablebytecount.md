# readBuffersAvailableByteCount

**Framework**: Virtualization  
**Kind**: property

The size of the read buffers memory (in bytes) exposed by the Virtio queue element that’s currently available for reading.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var readBuffersAvailableByteCount: Int { get }
```

#### Discussion

This value is initially equal to [`readBuffersByteCount`](vzvirtioqueueelement/readbuffersbytecount.md). This value decreases as you read memory from the read buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/readbuffersavailablebytecount)*