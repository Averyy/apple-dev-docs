# init

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_driver, bool in_is_settable, uint32_t in_control_value, IOUserVideoSliderRange in_range, IOUserVideoObjectPropertyElement in_control_element, IOUserVideoObjectPropertyScope in_control_scope, IOUserVideoClassID in_control_class_id);
```

#### Return Value

True on success.

#### Discussion

Initializes a IOUserVideoSliderControl.

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_is_settable`: A bool value indicating if the control value can be set
- `in_control_value`: A uint32_t for the control’s current slider value
- `in_range`: The IOUserVideoSliderRange for control
- `in_control_element`: The IOUserVideoObjectPropertyElement for the control
- `in_control_scope`: The IOUserVideoObjectPropertyScope for the control
- `in_control_class_id`: The IOUserVideoClassID of the control

## See Also

- [Create](iouservideoslidercontrol/create.md)
- [IOUserVideoDriver](iouservideodriver.md)
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoslidercontrol/init)*