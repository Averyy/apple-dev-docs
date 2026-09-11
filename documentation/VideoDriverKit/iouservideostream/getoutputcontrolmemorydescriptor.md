# GetOutputControlMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method

Gets the memory descriptor used for the control data part of a buffer.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
OSSharedPtr<IOMemoryDescriptor> GetOutputControlMemoryDescriptor(IOUserVideoObjectID in_object_id);
```

#### Return Value

IOMemoryDescriptor in an OSSharedPtr.

## Parameters

- `in_object_id`: The object identifier of the control portion of the desired buffer.

## See Also

- [GetOutputDataMemoryDescriptor](iouservideostream/getoutputdatamemorydescriptor.md)
  Gets the memory descriptor used for the video data part of a buffer.
- [GetOutputQueueMemoryDescriptor](iouservideostream/getoutputqueuememorydescriptor.md)
  Returns an memory descriptorrepesenting the shared memory output queue buffer.
- [GetInputQueueMemoryDescriptor](iouservideostream/getinputqueuememorydescriptor.md)
  Returns an memory descriptor for the shared memory input queue buffer.
- [GetMemoryObjectID](iouservideostream/getmemoryobjectid.md)
  Gets the video object identifier for a memory object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getoutputcontrolmemorydescriptor)*