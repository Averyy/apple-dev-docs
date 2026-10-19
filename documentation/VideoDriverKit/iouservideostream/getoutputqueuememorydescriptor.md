# GetOutputQueueMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method

Returns an memory descriptorrepesenting the shared memory output queue buffer.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
OSSharedPtr<IOMemoryDescriptor> GetOutputQueueMemoryDescriptor();
```

## See Also

- [GetOutputControlMemoryDescriptor](iouservideostream/getoutputcontrolmemorydescriptor.md)
  Gets the memory descriptor used for the control data part of a buffer.
- [GetOutputDataMemoryDescriptor](iouservideostream/getoutputdatamemorydescriptor.md)
  Gets the memory descriptor used for the video data part of a buffer.
- [GetInputQueueMemoryDescriptor](iouservideostream/getinputqueuememorydescriptor.md)
  Returns an memory descriptor for the shared memory input queue buffer.
- [GetMemoryObjectID](iouservideostream/getmemoryobjectid.md)
  Gets the video object identifier for a memory object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getoutputqueuememorydescriptor)*