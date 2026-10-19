# GetMemoryObjectID

**Framework**: VideoDriverKit  
**Kind**: method

Gets the video object identifier for a memory object.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
IOUserVideoObjectID GetMemoryObjectID(uint32_t memtype);
```

#### Return Value

The object identifier of the data portion of the buffer.

## Parameters

- `memtype`: A value encoding the memory object’s category in the upper 16 bits and, if needed, an index in the lower 16 bits.

## See Also

- [GetOutputControlMemoryDescriptor](iouservideostream/getoutputcontrolmemorydescriptor.md)
  Gets the memory descriptor used for the control data part of a buffer.
- [GetOutputDataMemoryDescriptor](iouservideostream/getoutputdatamemorydescriptor.md)
  Gets the memory descriptor used for the video data part of a buffer.
- [GetOutputQueueMemoryDescriptor](iouservideostream/getoutputqueuememorydescriptor.md)
  Returns an memory descriptorrepesenting the shared memory output queue buffer.
- [GetInputQueueMemoryDescriptor](iouservideostream/getinputqueuememorydescriptor.md)
  Returns an memory descriptor for the shared memory input queue buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getmemoryobjectid)*