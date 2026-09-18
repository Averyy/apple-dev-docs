# GetDataMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method

Gets the memory descriptor used for video IO that was initialized with or set on the video stream.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<IOMemoryDescriptor> GetDataMemoryDescriptor();
```

#### Return Value

IOMemoryDescriptor in an OSSharedPtr.

## See Also

- [SetDataMemoryDescriptor](iouservideobuffer/setdatamemorydescriptor.md)
  Sets a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.
- [SetControlMemoryDescriptor](iouservideobuffer/setcontrolmemorydescriptor.md)
  Sets a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.
- [GetControlMemoryDescriptor](iouservideobuffer/getcontrolmemorydescriptor.md)
  Gets the memory descriptior used for video IO that was initialized with or set on the video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer/getdatamemorydescriptor)*