# Create

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit 27.0+

## Declaration

```c
static OSSharedPtr<IOUserVideoBuffer> Create(IOUserVideoDriver *in_driver, IOUserVideoStreamDirection in_direction, IOMemoryDescriptor *in_data_memory_descriptor, IOMemoryDescriptor *in_control_memory_descriptor, uint32_t bufferID);
```

## See Also

### Creating a video buffer
- [init](./init.md)
- [IOUserVideoDriver](../iouservideodriver.md)
  A video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer/create)*