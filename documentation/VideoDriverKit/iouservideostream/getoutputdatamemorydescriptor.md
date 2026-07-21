# GetOutputDataMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<IOMemoryDescriptor> GetOutputDataMemoryDescriptor(IOUserVideoObjectID in_object_id);
```

#### Return Value

Returns IOMemoryDescriptor in an OSSharedPtr.

#### Discussion

Get the IOMemoryDescriptor used for the video data part of the IOVideoUserBuffer given the IOUserVideoObjectID

## Parameters

- `in_object_id`: The IOUserVideoObjectID of data portion of the desired IOUserVideoBuffer

## See Also

- [GetOutputControlMemoryDescriptor](iouservideostream/getoutputcontrolmemorydescriptor.md)
- [GetOutputQueueMemoryDescriptor](iouservideostream/getoutputqueuememorydescriptor.md)
- [GetInputQueueMemoryDescriptor](iouservideostream/getinputqueuememorydescriptor.md)
- [GetMemoryObjectID](iouservideostream/getmemoryobjectid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getoutputdatamemorydescriptor)*