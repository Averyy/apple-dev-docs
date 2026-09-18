# Create

**Framework**: VideoDriverKit  
**Kind**: method

A static factory method that allocates and initializes a video device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
static OSSharedPtr<IOUserVideoDevice> Create(IOUserVideoDriver *in_driver, OSString *in_device_uid, OSString *in_model_uid, OSString *in_manufacturer_uid);
```

#### Return Value

OSSharedPtr to an IOUserVideoDevice if it was successfully allocated and initialized

#### Discussion

If IOUserVideoDevice is subclassed to override behavior, don’t use this method to allocate or initialize the custom subclass.

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_device_uid`: OSString pointer for the video device unique identifier.
- `in_model_uid`: OSString pointer for the video device model unique identifier.
- `in_manufacturer_uid`: OSString pointer for the video device manufacturer unique identifier. *

## See Also

- [init](iouservideodevice/init.md)
  Initializes a video device.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/create)*