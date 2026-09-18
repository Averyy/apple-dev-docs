# IOUserVideoLevelControl

**Framework**: VideoDriverKit  
**Kind**: class

A control object that supports a float value level.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoLevelControl;
```

#### Overview

Getting/Setting control values can be done with scalar or decibel level values.

## Topics

### Creating a level control
- [Create](iouservideolevelcontrol/create.md)
  A static factory method that allocates and initializes a video level control.
- [init](iouservideolevelcontrol/init.md)
  Initializes an video level control.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoLevelControlRange](iouservideolevelcontrolrange.md)
  A control that supports a range of floating-point values.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.
### Freeing a level control
- [free](iouservideolevelcontrol/free.md)
  Frees the video level control.
### Getting information about the class
- [GetClassID](iouservideolevelcontrol/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideolevelcontrol/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Supporting value changes
- [HandleChangeDecibelValue](iouservideolevelcontrol/handlechangedecibelvalue.md)
  The system calls this virtual method when the control’s value changes.
- [HandleChangeScalarValue](iouservideolevelcontrol/handlechangescalarvalue.md)
  The system calls this virtual method when the control’s value changes.
### Accessing the value
- [SetScalarValue](iouservideolevelcontrol/setscalarvalue.md)
  Sets the current scalar level value.
- [SetDecibelValue](iouservideolevelcontrol/setdecibelvalue.md)
  Sets the current decibel level value.
- [GetScalarValue](iouservideolevelcontrol/getscalarvalue.md)
  Gets the scalar level value for the control.
- [GetDecibelValue](iouservideolevelcontrol/getdecibelvalue.md)
  Gets the decibel level value for the control.

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
- [IOUserVideoDirectionControl](iouservideodirectioncontrol.md)
  A control object that supports Boolean values.
- [IOUserVideoSelectorControl](iouservideoselectorcontrol.md)
  A control object that supports a 32-bit unsigned integer selector value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol)*