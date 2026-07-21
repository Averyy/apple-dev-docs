# GetDataMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<IOMemoryDescriptor> GetDataMemoryDescriptor();
```

#### Return Value

Returns IOMemoryDescriptor in an OSSharedPtr.

#### Discussion

Get the IOMemoryDescriptor used for video IO that was initialied with or set on the video stream

## See Also

- [SetDataMemoryDescriptor](iouservideobuffer/setdatamemorydescriptor.md)
- [SetControlMemoryDescriptor](iouservideobuffer/setcontrolmemorydescriptor.md)
- [GetControlMemoryDescriptor](iouservideobuffer/getcontrolmemorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer/getdatamemorydescriptor)*