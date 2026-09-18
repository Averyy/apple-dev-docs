# IOUserVideoSelectorControl

**Framework**: VideoDriverKit  
**Kind**: class

A control object that supports a 32-bit unsigned integer selector value.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoSelectorControl;
```

## Topics

### Creating a selector control
- [Create](iouservideoselectorcontrol/create.md)
  A static factory method that allocates and initializes a selector control.
- [init](iouservideoselectorcontrol/init.md)
  Initializes a selector control.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
  An integer that identifies, along with the property selector and scope, a specific piece of information about a video object.
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
  A four character code which, along with the selector and element, identifies a specific piece of information about a video object.
### Freeing a selector control
- [free](iouservideoselectorcontrol/free.md)
  Frees the selector control.
### Getting information about the class
- [GetClassID](iouservideoselectorcontrol/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideoselectorcontrol/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Supporting value changes
- [HandleChangeSelectedValues](iouservideoselectorcontrol/handlechangeselectedvalues.md)
  The system calls this virtual method when the control’s selected values change.
### Accessing the value
- [SetCurrentSelectedValues](iouservideoselectorcontrol/setcurrentselectedvalues.md)
  Sets the current control value.
- [GetCurrentSelectedValues](iouservideoselectorcontrol/getcurrentselectedvalues.md)
  Gets the current selected values of the control.
- [IOUserVideoSelectorValue](iouservideoselectorvalue.md)
  Selector value for controls.
- [GetControlValuesCount](iouservideoselectorcontrol/getcontrolvaluescount.md)
  Gets the number of available selector control values.
- [AddControlValueDescriptions](iouservideoselectorcontrol/addcontrolvaluedescriptions.md)
  Adds control value descriptions to the selector control.
- [RemoveControlValueDescriptions](iouservideoselectorcontrol/removecontrolvaluedescriptions.md)
  Removes selector control values from the selector control.
- [GetControlValueDescriptions](iouservideoselectorcontrol/getcontrolvaluedescriptions.md)
  Gets the selector values for the control.
- [IOUserVideoSelectorValueDescription](iouservideoselectorvaluedescription.md)
  A selector control’s value and name.

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
- [IOUserVideoLevelControl](iouservideolevelcontrol.md)
  A control object that supports a float value level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol)*