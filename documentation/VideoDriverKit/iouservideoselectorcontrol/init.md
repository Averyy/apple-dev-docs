# init

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_driver, bool in_is_settable, IOUserVideoObjectPropertyElement in_control_element, IOUserVideoObjectPropertyScope in_control_scope, IOUserVideoClassID in_control_class_id);
```

#### Return Value

True on success.

#### Discussion

Initializes a IOUserVideoSelectorControl.

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_is_settable`: A bool value indicating if the control value can be set
- `in_control_element`: The IOUserVideoObjectPropertyElement for the control
- `in_control_scope`: The IOUserVideoObjectPropertyScope for the control
- `in_control_class_id`: The IOUserVideoClassID of the control

## See Also

- [Create](iouservideoselectorcontrol/create.md)
- [IOUserVideoDriver](iouservideodriver.md)
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/init)*