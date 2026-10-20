# SetControlMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetControlMemoryDescriptor(IOMemoryDescriptor *in_control_memory_descriptor);
```

#### Discussion

Setting this value should only be done during the PerformDeviceConfigurationChange() call. If the value needs to be changed, RequestDeviceConfigChange() should be called to allow IO to stop and the config change to be performed.

## Parameters

- `in_control_memory_descriptor`: A pointer to a IOMemoryDescriptor whose buffer will be mapped to the Host for doing video IO

## See Also

### Working with memory descriptors
- [SetDataMemoryDescriptor](./setdatamemorydescriptor.md)
  Sets a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.
- [GetDataMemoryDescriptor](./getdatamemorydescriptor.md)
  Gets the memory descriptor used for video IO that was initialized with or set on the video stream.
- [GetControlMemoryDescriptor](./getcontrolmemorydescriptor.md)
  Gets the memory descriptior used for video IO that was initialized with or set on the video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer/setcontrolmemorydescriptor)*