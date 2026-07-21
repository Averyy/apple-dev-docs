# Create

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
static OSSharedPtr<IOUserVideoDevice> Create(IOUserVideoDriver *in_driver, OSString *in_device_uid, OSString *in_model_uid, OSString *in_manufacturer_uid);
```

#### Return Value

OSSharedPtr to an IOUserVideoDevice if it was successfully allocated and initialized

#### Discussion

Static factory method to allocate and initialize an IOUserVideoDevice.

If IOUserVideoDevice is subclassed to override behavior, Create should not be used to allocate/initialize the custom subclass.

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_device_uid`: OSString pointer for the video device unique identifier.
- `in_model_uid`: OSString pointer for the video device model unique identifier.
- `in_manufacturer_uid`: OSString pointer for the video device manufacturer unique identifier. *

## See Also

- [init](iouservideodevice/init.md)
- [IOUserVideoDriver](iouservideodriver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/create)*