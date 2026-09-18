# IOUserVideoSliderControl

**Framework**: VideoDriverKit  
**Kind**: class

A control object that supports a 32-bit unsigned integer value slider.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoSliderControl;
```

## Topics

### Creating a slider control
- [Create](iouservideoslidercontrol/create.md)
  A static factory method that allocates and initializes an slider control.
- [init](iouservideoslidercontrol/init.md)
  Initializes a slider control.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.
### Freeing a slider control
- [free](iouservideoslidercontrol/free.md)
  Frees the slider control.
### Getting information about the class
- [GetClassID](iouservideoslidercontrol/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideoslidercontrol/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Supporting value changes
- [HandleChangeControlValue](iouservideoslidercontrol/handlechangecontrolvalue.md)
  The system calls this virtual method when the control’s value changes.
### Accessing the value
- [SetControlValue](iouservideoslidercontrol/setcontrolvalue.md)
  Sets the current control value.
- [GetControlValue](iouservideoslidercontrol/getcontrolvalue.md)
  Gets the current value of the control.
- [SetRange](iouservideoslidercontrol/setrange.md)
  Sets the current range of the slider control.
- [GetRange](iouservideoslidercontrol/getrange.md)
  Gets the current range of the slider control.
- [IOUserVideoSliderRange](iouservideosliderrange.md)
  The minimum and maximum range for the slider value.

## Relationships

### Inherits From
- [IOUserVideoControl](iouservideocontrol.md)

## See Also

- [IOUserVideoControl](iouservideocontrol.md)
  A base class for control objects.
- [IOUserVideoBooleanControl](iouservideobooleancontrol.md)
  A control object that supports Boolean values.
- [IOUserVideoStereoPanControl](iouservideostereopancontrol.md)
  A control object that supports panning between stereo channels.
- [IOUserVideoDirectionControl](iouservideodirectioncontrol.md)
  A control object that supports Boolean values.
- [IOUserVideoSelectorControl](iouservideoselectorcontrol.md)
  A control object that supports a 32-bit unsigned integer selector value.
- [IOUserVideoLevelControl](iouservideolevelcontrol.md)
  A control object that supports a float value level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoslidercontrol)*