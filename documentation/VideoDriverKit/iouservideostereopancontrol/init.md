# init

**Framework**: VideoDriverKit  
**Kind**: method

Initializes an stereo pan control.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_driver, bool in_is_settable, float in_control_value, IOUserVideoObjectPropertyElement in_left_channel, IOUserVideoObjectPropertyElement in_right_channel, IOUserVideoObjectPropertyElement in_control_element, IOUserVideoObjectPropertyScope in_control_scope, IOUserVideoClassID in_control_class_id);
```

#### Return Value

True on success.

## Parameters

- `in_driver`: The video driver that owns this object.
- `in_is_settable`: A Boolean value indicating whether the control value can be set.
- `in_control_value`: The control’s current stereo pan value.
- `in_left_channel`: The property element for the left channel.
- `in_right_channel`: The property element for the right channel.
- `in_control_element`: The property element for the control.
- `in_control_scope`: The property scope for the control.
- `in_control_class_id`: The class ID of the control.

## See Also

- [Create](iouservideostereopancontrol/create.md)
  A static factory method that allocates and initializes an stereo pan control.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol/init)*