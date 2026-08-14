# peekIntoReadBuffers(withExactLength:)

**Framework**: Virtualization  
**Kind**: method

Peeks into the read buffers and copy exactLength bytes from the read buffer into the data object it returns.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func peekIntoReadBuffers(withExactLength exactLength: Int) throws -> Data
```

#### Return Value

An [`NSData`](https://developer.apple.com/documentation/foundation/nsdata) object filled with the memory that the framework copied, or `nil` if the peek failed.

#### Discussion

This method allows you to peek into the read buffers without consuming any of the memory, [`readBuffersAvailableByteCount`](vzvirtioqueueelement/readbuffersavailablebytecount.md) does not change after this call.

## Parameters

- `exactLength`: Number of bytes to copy from the read buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/peekintoreadbuffers(withexactlength:))*