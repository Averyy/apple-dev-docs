# IOUserVideoStereoPanControl

**Framework**: VideoDriverKit  
**Kind**: class

A control object that supports panning between stereo channels.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
class IOUserVideoStereoPanControl;
```

## Topics

### Creating a stereo pan control
- [Create](iouservideostereopancontrol/create.md)
  A static factory method that allocates and initializes an stereo pan control.
- [init](iouservideostereopancontrol/init.md)
  Initializes an stereo pan control.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.
### Freeing a stereo pan control
- [free](iouservideostereopancontrol/free.md)
  Frees the stereo pan control.
### Getting information about the class
- [GetClassID](iouservideostereopancontrol/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideostereopancontrol/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Supporting value changes
- [HandleChangeControlValue](iouservideostereopancontrol/handlechangecontrolvalue.md)
  The system calls this virtual method when the control’s value changes.
### Accessing the value
- [SetControlValue](iouservideostereopancontrol/setcontrolvalue.md)
  Sets the current control value.
- [GetControlValue](iouservideostereopancontrol/getcontrolvalue.md)
  Gets the current value of the control.
- [SetPanningChannels](iouservideostereopancontrol/setpanningchannels.md)
  Sets the current stereo panning channels.
- [GetPanningChannels](iouservideostereopancontrol/getpanningchannels.md)
  Gets the current stereo panning channels.

## Relationships

### Inherits From
- [IOUserVideoControl](iouservideocontrol.md)

## See Also

- [IOUserVideoControl](iouservideocontrol.md)
  A base class for control objects.
- [IOUserVideoBooleanControl](iouservideobooleancontrol.md)
  A control object that supports Boolean values.
- [IOUserVideoSliderControl](iouservideoslidercontrol.md)
  A control object that supports a 32-bit unsigned integer value slider.
- [IOUserVideoDirectionControl](iouservideodirectioncontrol.md)
  A control object that supports Boolean values.
- [IOUserVideoSelectorControl](iouservideoselectorcontrol.md)
  A control object that supports a 32-bit unsigned integer selector value.
- [IOUserVideoLevelControl](iouservideolevelcontrol.md)
  A control object that supports a float value level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol)*