# readBuffers()

**Framework**: Virtualization  
**Kind**: method

Gets the remaining read buffers memory represented as an array of data.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func readBuffers() -> [Data]
```

#### Return Value

An array of [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object that represents the remaining read buffers memory.

#### Discussion

This method gets the remaining read buffers memory, after calling this method, [`readBuffersAvailableByteCount`](vzvirtioqueueelement/readbuffersavailablebytecount.md) will be zero, behaving as if you have read all of the read buffers available in the [`VZVirtioQueueElement`](vzvirtioqueueelement.md).

Here, the memory is represented as scatter-gather buffers directly referencing guest memory without any extra copy.

> ❗ **Important**: It’s strongly recommended to access the underlying memory only once. Accessing this memory multiple times can introduce time-of-check, time-of-use (TOCTOU) bugs which are prone to security attacks. Since the guest is free to modify its memory at any time, two consecutive reads may return different results, and malicious guests can take advantage of this to perform various attacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/readbuffers())*