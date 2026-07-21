# Create

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
static OSSharedPtr<IOUserVideoLevelControl> Create(IOUserVideoDriver *in_driver, bool in_is_settable, float in_decibel_value, IOUserVideoLevelControlRange in_decibel_range, IOUserVideoObjectPropertyElement in_control_element, IOUserVideoObjectPropertyScope in_control_scope, IOUserVideoClassID in_control_class_id);
```

#### Return Value

OSSharedPtr to an IOUserVideoLevelControl if it was successfully allocated and initialized

#### Discussion

Static factory method to allocate and initialize an IOUserVideoLevelControl.

If IOUserVideoLevelControl is subclassed to override behavior, Create should not be used to allocate/initialize the custom subclass.

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_is_settable`: A bool value indicating if the control value can be set
- `in_decibel_value`: A float for the controls current decibel level value
- `in_decibel_range`: A IOUserVideoLevelControlRange for the controls decibe minimum and maximum range
- `in_control_element`: The IOUserVideoObjectPropertyElement for the control
- `in_control_scope`: The IOUserVideoObjectPropertyScope for the control
- `in_control_class_id`: The IOUserVideoClassID of the control

## See Also

- [init](iouservideolevelcontrol/init.md)
- [IOUserVideoDriver](iouservideodriver.md)
- [IOUserVideoLevelControlRange](iouservideolevelcontrolrange.md)
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol/create)*