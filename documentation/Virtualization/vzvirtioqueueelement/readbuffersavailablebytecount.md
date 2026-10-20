# readBuffersAvailableByteCount

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The size of the read buffers memory (in bytes) exposed by the Virtio queue element that’s currently available for reading.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var readBuffersAvailableByteCount: Int { get }
```

```objc
@property (readonly) NSUInteger readBuffersAvailableByteCount;
```

#### Discussion

This value is initially equal to [`readBuffersByteCount`](./readbuffersbytecount.md). This value decreases as you read memory from the read buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/readbuffersavailablebytecount)*