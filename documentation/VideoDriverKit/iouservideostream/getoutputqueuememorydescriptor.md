# GetOutputQueueMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns an memory descriptorrepesenting the shared memory output queue buffer.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
OSSharedPtr<IOMemoryDescriptor> GetOutputQueueMemoryDescriptor();
```

## See Also

### Working with memory descriptors
- [GetOutputControlMemoryDescriptor](./getoutputcontrolmemorydescriptor.md)
  Gets the memory descriptor used for the control data part of a buffer.
- [GetOutputDataMemoryDescriptor](./getoutputdatamemorydescriptor.md)
  Gets the memory descriptor used for the video data part of a buffer.
- [GetInputQueueMemoryDescriptor](./getinputqueuememorydescriptor.md)
  Returns an memory descriptor for the shared memory input queue buffer.
- [GetMemoryObjectID](./getmemoryobjectid.md)
  Gets the video object identifier for a memory object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getoutputqueuememorydescriptor)*