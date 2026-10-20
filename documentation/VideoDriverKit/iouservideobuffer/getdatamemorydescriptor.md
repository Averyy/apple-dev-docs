# GetDataMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the memory descriptor used for video IO that was initialized with or set on the video stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
OSSharedPtr<IOMemoryDescriptor> GetDataMemoryDescriptor();
```

#### Return Value

IOMemoryDescriptor in an OSSharedPtr.

## See Also

### Working with memory descriptors
- [SetDataMemoryDescriptor](./setdatamemorydescriptor.md)
  Sets a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.
- [SetControlMemoryDescriptor](./setcontrolmemorydescriptor.md)
  Sets a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.
- [GetControlMemoryDescriptor](./getcontrolmemorydescriptor.md)
  Gets the memory descriptior used for video IO that was initialized with or set on the video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer/getdatamemorydescriptor)*