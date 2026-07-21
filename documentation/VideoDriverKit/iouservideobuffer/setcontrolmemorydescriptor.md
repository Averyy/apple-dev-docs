# SetControlMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetControlMemoryDescriptor(IOMemoryDescriptor *in_control_memory_descriptor);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.

Setting this value should only be done during the PerformDeviceConfigurationChange() call. If the value needs to be changed, RequestDeviceConfigChange() should be called to allow IO to stop and the config change to be performed.

## Parameters

- `in_control_memory_descriptor`: A pointer to a IOMemoryDescriptor whose buffer will be mapped to the Host for doing video IO

## See Also

- [SetDataMemoryDescriptor](iouservideobuffer/setdatamemorydescriptor.md)
- [GetDataMemoryDescriptor](iouservideobuffer/getdatamemorydescriptor.md)
- [GetControlMemoryDescriptor](iouservideobuffer/getcontrolmemorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer/setcontrolmemorydescriptor)*