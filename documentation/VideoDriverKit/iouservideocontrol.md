# IOUserVideoControl

**Framework**: VideoDriverKit  
**Kind**: class

A base class for control objects.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
class IOUserVideoControl;
```

#### Overview

Don’t subclass [`IOUserVideoControl`](iouservideocontrol.md) or allocated instances directly.

## Topics

### Creating a control
- [init](iouservideocontrol/init.md)
  Initializes a video control.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.
### Freeing a control
- [free](iouservideocontrol/free.md)
  Frees the user video object.
### Getting information about the class
- [GetClassID](iouservideocontrol/getclassid.md)
  Gets the class identifier of the object
- [GetBaseClassID](iouservideocontrol/getbaseclassid.md)
  Gets the class identifier of the base class object
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Working with control properties
- [GetControlScope](iouservideocontrol/getcontrolscope.md)
  Returns an object property scope for the control.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [GetControlElement](iouservideocontrol/getcontrolelement.md)
  Returns an object property element for the control.
- [GetIsSettable](iouservideocontrol/getissettable.md)
  Returns a Boolean value indicating if the control value can be set.
### Working with devices
- [GetOwningDeviceID](iouservideocontrol/getowningdeviceid.md)
  Returns the video object identifier of the control’s owning device.

## Relationships

### Inherits From
- [IOUserVideoObject](iouservideoobject.md)
### Inherited By
- [IOUserVideoBooleanControl](iouservideobooleancontrol.md)
- [IOUserVideoDirectionControl](iouservideodirectioncontrol.md)
- [IOUserVideoLevelControl](iouservideolevelcontrol.md)
- [IOUserVideoSelectorControl](iouservideoselectorcontrol.md)
- [IOUserVideoSliderControl](iouservideoslidercontrol.md)
- [IOUserVideoStereoPanControl](iouservideostereopancontrol.md)

## See Also

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
- [IOUserVideoLevelControl](iouservideolevelcontrol.md)
  A control object that supports a float value level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocontrol)*