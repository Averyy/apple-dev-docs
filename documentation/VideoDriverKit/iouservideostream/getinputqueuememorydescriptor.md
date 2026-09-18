# GetInputQueueMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method

Returns an memory descriptor for the shared memory input queue buffer.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<IOMemoryDescriptor> GetInputQueueMemoryDescriptor();
```

## See Also

- [GetOutputControlMemoryDescriptor](iouservideostream/getoutputcontrolmemorydescriptor.md)
  Gets the memory descriptor used for the control data part of a buffer.
- [GetOutputDataMemoryDescriptor](iouservideostream/getoutputdatamemorydescriptor.md)
  Gets the memory descriptor used for the video data part of a buffer.
- [GetOutputQueueMemoryDescriptor](iouservideostream/getoutputqueuememorydescriptor.md)
  Returns an memory descriptorrepesenting the shared memory output queue buffer.
- [GetMemoryObjectID](iouservideostream/getmemoryobjectid.md)
  Gets the video object identifier for a memory object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getinputqueuememorydescriptor)*