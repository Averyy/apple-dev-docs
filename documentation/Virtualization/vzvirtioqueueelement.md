# VZVirtioQueueElement

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A unit of work on a Virtio queue, also known as a descriptor chain.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZVirtioQueueElement
```

```objc
@interface VZVirtioQueueElement : NSObject
```

#### Overview

A `VZVirtioQueueElement` represents a unit of work from a [`VZVirtioQueue`](./vzvirtioqueue.md) with which it’s associated, facilitating device operations specified by the [`VZCustomVirtioDevice`](./vzcustomvirtiodevice.md) that the `VZVirtioQueue` belongs to. It exposes the scatter-gather memory to the guest’s dynamic random access memory (DRAM) that the Virtio queue references as read buffers and write buffers; this allows for read-only and write-only access, respectively, to this memory on the host. It’s strongly recommended to access the read buffers and write buffers only *once* using the [`readBytes(withExactLength:)`](./vzvirtioqueueelement/readbytes%28withexactlength%29.md), [`readBytes(intoBuffer:exactLength:)`](./vzvirtioqueueelement/readbytes%28intobuffer,exactlength%29.md), [`write(_:)`](./vzvirtioqueueelement/write%28_%29.md), and [`writeBuffer(_:exactLength:)`](./vzvirtioqueueelement/writebuffer%28_,exactlength%29.md) methods. Those methods enforce that you only access the memory once and changes the value of [`readBuffersAvailableByteCount`](./vzvirtioqueueelement/readbuffersavailablebytecount.md) and [`writeBuffersAvailableByteCount`](./vzvirtioqueueelement/writebuffersavailablebytecount.md) accordingly. The [`peekIntoReadBuffers(withExactLength:)`](./vzvirtioqueueelement/peekintoreadbuffers%28withexactlength%29.md) method allows for multiple read accesses if absolutely necessary and doesn’t change the value of [`readBuffersAvailableByteCount`](./vzvirtioqueueelement/readbuffersavailablebytecount.md).

> ❗ **Important**: Accessing this memory multiple times can introduce time-of-check time-of-use (TOCTOU) bugs which are prone to security attacks. Since the guest is free to modify its memory at any time, two consecutive reads may return different results, and malicious guests can take advantage of this to perform various attacks.

Don’t instantiate `VZVirtioQueueElement` objects directly, the framework provides them through the [`nextElement()`](./vzvirtioqueue/nextelement%28%29.md) method when you handle any elements in the Virtio queue. When you are done with processing the element, you need to call [`returnToQueue()`](./vzvirtioqueueelement/returntoqueue%28%29.md) to return the element back to the guest.

## Topics

### Instance Properties
- [var readBuffersAvailableByteCount: Int](./vzvirtioqueueelement/readbuffersavailablebytecount.md)
  The size of the read buffers memory (in bytes) exposed by the Virtio queue element that’s currently available for reading.
- [var readBuffersByteCount: Int](./vzvirtioqueueelement/readbuffersbytecount.md)
  The total size of the read buffers memory (in bytes) exposed by the Virtio queue element.
- [var writeBuffersAvailableByteCount: Int](./vzvirtioqueueelement/writebuffersavailablebytecount.md)
  The size of the write buffers memory (in bytes) exposed by the Virtio queue element that’s currently available for writing.
- [var writeBuffersByteCount: Int](./vzvirtioqueueelement/writebuffersbytecount.md)
  The total size of the write buffers memory (in bytes) exposed by the Virtio queue element.
- [var writtenByteCount: Int](./vzvirtioqueueelement/writtenbytecount.md)
  The size of the write buffers memory exposed (in bytes) by the Virtio queue element that has already been written to.
### Instance Methods
- [func peekIntoReadBuffers(withExactLength: Int) throws -> Data](./vzvirtioqueueelement/peekintoreadbuffers%28withexactlength%29.md)
  Peeks into the read buffers and copy exactLength bytes from the read buffer into the data object it returns.
- [func readBuffers() -> [Data]](./vzvirtioqueueelement/readbuffers%28%29.md)
  Gets the remaining read buffers memory represented as an array of data.
- [func readBytes(intoBuffer: UnsafeMutableRawPointer, exactLength: Int) throws](./vzvirtioqueueelement/readbytes%28intobuffer,exactlength%29.md)
  Reads the number of bytes you specify from the read buffers into the memory pointed to by the pointer to the buffer you provide.
- [func readBytes(withExactLength: Int) throws -> Data](./vzvirtioqueueelement/readbytes%28withexactlength%29.md)
  Reads the number of bytes you specify from the read buffers and return result as a data object.
- [func returnToQueue()](./vzvirtioqueueelement/returntoqueue%28%29.md)
  Returns this element back to the guest.
- [func write(Data) throws](./vzvirtioqueueelement/write%28_%29.md)
  Writes the memory represented by the data object you provide into the write buffers.
- [func writeBuffer(UnsafeMutableRawPointer, exactLength: Int) throws](./vzvirtioqueueelement/writebuffer%28_,exactlength%29.md)
  Writes to the memory represented by the pointer to the buffer you provide to the write buffers.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZCustomVirtioDevice](./vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
- [class VZVirtioQueue](./vzvirtioqueue.md)
  A Virtio queue.
### Working with VirtQueues
- [class VZVirtioQueue](./vzvirtioqueue.md)
  A Virtio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement)*