# Create

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
static OSSharedPtr<IOUserVideoBuffer> Create(IOUserVideoDriver *in_driver, IOUserVideoStreamDirection in_direction, IOMemoryDescriptor *in_data_memory_descriptor, IOMemoryDescriptor *in_control_memory_descriptor, uint32_t bufferID);
```

## See Also

- [init](iouservideobuffer/init.md)
- [IOUserVideoDriver](iouservideodriver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer/create)*