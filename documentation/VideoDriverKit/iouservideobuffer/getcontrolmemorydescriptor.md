# GetControlMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<IOMemoryDescriptor> GetControlMemoryDescriptor();
```

#### Return Value

Returns IOMemoryDescriptor in an OSSharedPtr.

#### Discussion

Get the IOMemoryDescriptor used for video IO that was initialied with or set on the video stream

## See Also

- [SetDataMemoryDescriptor](iouservideobuffer/setdatamemorydescriptor.md)
- [GetDataMemoryDescriptor](iouservideobuffer/getdatamemorydescriptor.md)
- [SetControlMemoryDescriptor](iouservideobuffer/setcontrolmemorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer/getcontrolmemorydescriptor)*