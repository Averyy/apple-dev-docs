# GetMemoryObjectID

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
IOUserVideoObjectID GetMemoryObjectID(uint32_t memtype);
```

#### Return Value

Returns IOUserVideoObjectID of the data portion of the IOUserVideoBuffer.

#### Discussion

Get the IOUserVideoObjectID for the memory object given the memtype which is a catagory in the upper 16bits and an index if needed in the lower 16 bits

## Parameters

- `memtype`: The IOUserVideoObjectID of the memory specified  by the memtype

## See Also

- [GetOutputControlMemoryDescriptor](iouservideostream/getoutputcontrolmemorydescriptor.md)
- [GetOutputDataMemoryDescriptor](iouservideostream/getoutputdatamemorydescriptor.md)
- [GetOutputQueueMemoryDescriptor](iouservideostream/getoutputqueuememorydescriptor.md)
- [GetInputQueueMemoryDescriptor](iouservideostream/getinputqueuememorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getmemoryobjectid)*