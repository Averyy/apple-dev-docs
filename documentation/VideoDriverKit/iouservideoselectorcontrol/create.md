# Create

**Framework**: VideoDriverKit  
**Kind**: method

A static factory method that allocates and initializes a selector control.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
static OSSharedPtr<IOUserVideoSelectorControl> Create(IOUserVideoDriver *in_driver, bool in_is_settable, IOUserVideoObjectPropertyElement in_control_element, IOUserVideoObjectPropertyScope in_control_scope, IOUserVideoClassID in_control_class_id);
```

#### Return Value

OSSharedPtr to an IOUserVideoSelectorControl if it was successfully allocated and initialized

#### Discussion

If IOUserVideoSelectorControl is subclassed to override behavior, don’t use this method to allocate or initialize the custom subclass.

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_is_settable`: A Boolean value indicating if the control value can be set
- `in_control_element`: The IOUserVideoObjectPropertyElement for the control
- `in_control_scope`: The IOUserVideoObjectPropertyScope for the control
- `in_control_class_id`: The IOUserVideoClassID of the control

## See Also

- [init](iouservideoselectorcontrol/init.md)
  Initializes a selector control.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/create)*