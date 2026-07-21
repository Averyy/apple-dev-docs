# init

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_driver, OSString *in_device_uid, OSString *in_model_uid, OSString *in_manufacturer_uid);
```

#### Return Value

True on success.

#### Discussion

Initializes a IOUserVideoDevice.

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_device_uid`: OSString pointer for the video device unique identifier.
- `in_model_uid`: OSString pointer for the video device model unique identifier.
- `in_manufacturer_uid`: OSString pointer for the video device manufacturer unique identifier. *

## See Also

- [Create](iouservideodevice/create.md)
- [IOUserVideoDriver](iouservideodriver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/init)*