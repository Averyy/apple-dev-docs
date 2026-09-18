# IOUserVideoBooleanControl

**Framework**: VideoDriverKit  
**Kind**: class

A control object that supports Boolean values.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoBooleanControl;
```

## Topics

### Creating a Boolean control
- [Create](iouservideobooleancontrol/create.md)
  A static factory method that allocates and initializes a video Boolean control.
- [init](iouservideobooleancontrol/init.md)
  Initializes an IOUserVideoBooleanControl.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.
### Freeing a Boolean control
- [free](iouservideobooleancontrol/free.md)
  Frees the control.
### Getting information about the class
- [GetClassID](iouservideobooleancontrol/getclassid.md)
  Gets the class identifier of the object
- [GetBaseClassID](iouservideobooleancontrol/getbaseclassid.md)
  Gets the class identifier of the base class object
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Supporting value changes
- [HandleChangeControlValue](iouservideobooleancontrol/handlechangecontrolvalue.md)
  The system calls this virtual method when the control’s value changes.
### Accessing the value
- [SetControlValue](iouservideobooleancontrol/setcontrolvalue.md)
  Sets the current control value.
- [GetControlValue](iouservideobooleancontrol/getcontrolvalue.md)
  Gets the current value of the control.

## Relationships

### Inherits From
- [IOUserVideoControl](iouservideocontrol.md)

## See Also

- [IOUserVideoControl](iouservideocontrol.md)
  A base class for control objects.
- [IOUserVideoStereoPanControl](iouservideostereopancontrol.md)
  A control object that supports panning between stereo channels.
- [IOUserVideoSliderControl](iouservideoslidercontrol.md)
  A control object that supports a 32-bit unsigned integer value slider.
- [IOUserVideoDirectionControl](iouservideodirectioncontrol.md)
  A control object that supports Boolean values.
- [IOUserVideoSelectorControl](iouservideoselectorcontrol.md)
  A control object that supports a 32-bit unsigned integer selector value.
- [IOUserVideoLevelControl](iouservideolevelcontrol.md)
  A control object that supports a float value level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobooleancontrol)*