# IOUserVideoDirectionControl

**Framework**: VideoDriverKit  
**Kind**: class

A control object that supports Boolean values.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoDirectionControl;
```

## Topics

### Creating a direction control
- [Create](iouservideodirectioncontrol/create.md)
  A static factory method that allocates and initializes a video direction control.
- [init](iouservideodirectioncontrol/init.md)
  Initializes a video direction control.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.
### Freeing a slider control
- [free](iouservideodirectioncontrol/free.md)
  Frees the video direction control.
### Getting information about the class
- [GetClassID](iouservideodirectioncontrol/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideodirectioncontrol/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Supporting value changes
- [HandleChangeControlValue](iouservideodirectioncontrol/handlechangecontrolvalue.md)
  The system calls this virtual method when the control’s value changes.
### Accessing the value
- [SetControlValue](iouservideodirectioncontrol/setcontrolvalue.md)
  Sets the current control value.
- [GetControlValue](iouservideodirectioncontrol/getcontrolvalue.md)
  Gets the current value of the control.

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
- [IOUserVideoSliderControl](iouservideoslidercontrol.md)
  A control object that supports a 32-bit unsigned integer value slider.
- [IOUserVideoSelectorControl](iouservideoselectorcontrol.md)
  A control object that supports a 32-bit unsigned integer selector value.
- [IOUserVideoLevelControl](iouservideolevelcontrol.md)
  A control object that supports a float value level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodirectioncontrol)*