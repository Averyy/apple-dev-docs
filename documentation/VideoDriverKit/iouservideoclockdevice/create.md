# Create

**Framework**: VideoDriverKit  
**Kind**: method

A static factory method that allocates and initializes a video clock device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
static OSSharedPtr<IOUserVideoClockDevice> Create(IOUserVideoDriver *in_driver, OSString *in_device_uid, OSString *in_model_uid, OSString *in_manufacturer_uid);
```

#### Return Value

OSSharedPtr to an IOUserVideoClockDevice if it was successfully allocated and initialized

#### Discussion

If IOUserVideoClockDevice is subclassed to override behavior, don’t use this method to allocate or initialize the custom subclass.

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_device_uid`: OSString pointer for the clock device unique identifier
- `in_model_uid`: OSString pointer for the clock device model unique identifier
- `in_manufacturer_uid`: OSString pointer for the clock device manufacturer unique identifier *

## See Also

- [init](iouservideoclockdevice/init.md)
  Initializes a video clock device.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/create)*