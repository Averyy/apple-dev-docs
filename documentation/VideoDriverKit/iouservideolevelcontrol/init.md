# init

**Framework**: VideoDriverKit  
**Kind**: method

Initializes an video level control.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_driver, bool in_is_settable, float in_decibel_value, IOUserVideoLevelControlRange in_decibel_range, IOUserVideoObjectPropertyElement in_control_element, IOUserVideoObjectPropertyScope in_control_scope, IOUserVideoClassID in_control_class_id);
```

#### Return Value

True on success.

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_is_settable`: A Boolean value indicating if the control value can be set
- `in_decibel_value`: A float for the controls current decibel level value
- `in_decibel_range`: A IOUserVideoLevelControlRange for the controls decibe minimum and maximum range
- `in_control_element`: The IOUserVideoObjectPropertyElement for the control
- `in_control_scope`: The IOUserVideoObjectPropertyScope for the control
- `in_control_class_id`: The IOUserVideoClassID of the control

## See Also

- [Create](iouservideolevelcontrol/create.md)
  A static factory method that allocates and initializes a video level control.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoLevelControlRange](iouservideolevelcontrolrange.md)
  A control that supports a range of floating-point values.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol/init)*