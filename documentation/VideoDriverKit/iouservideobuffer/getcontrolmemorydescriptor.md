# GetControlMemoryDescriptor

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the memory descriptior used for video IO that was initialized with or set on the video stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
OSSharedPtr<IOMemoryDescriptor> GetControlMemoryDescriptor();
```

## Return Value

IOMemoryDescriptor in an OSSharedPtr.

## See Also

### Working with memory descriptors
- [SetDataMemoryDescriptor](./setdatamemorydescriptor.md)
  Sets a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.
- [GetDataMemoryDescriptor](./getdatamemorydescriptor.md)
  Gets the memory descriptor used for video IO that was initialized with or set on the video stream.
- [SetControlMemoryDescriptor](./setcontrolmemorydescriptor.md)
  Sets a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer/getcontrolmemorydescriptor)*