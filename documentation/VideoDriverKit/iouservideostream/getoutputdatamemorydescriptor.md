# GetOutputDataMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the memory descriptor used for the video data part of a buffer.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
OSSharedPtr<IOMemoryDescriptor> GetOutputDataMemoryDescriptor(IOUserVideoObjectID in_object_id);
```

#### Return Value

The memory descriptor.

## Parameters

- `in_object_id`: The object identifier of the data portion of the desired buffer.

## See Also

### Working with memory descriptors
- [GetOutputControlMemoryDescriptor](./getoutputcontrolmemorydescriptor.md)
  Gets the memory descriptor used for the control data part of a buffer.
- [GetOutputQueueMemoryDescriptor](./getoutputqueuememorydescriptor.md)
  Returns an memory descriptorrepesenting the shared memory output queue buffer.
- [GetInputQueueMemoryDescriptor](./getinputqueuememorydescriptor.md)
  Returns an memory descriptor for the shared memory input queue buffer.
- [GetMemoryObjectID](./getmemoryobjectid.md)
  Gets the video object identifier for a memory object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getoutputdatamemorydescriptor)*