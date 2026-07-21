# IOUserVideoSelectorControl

**Framework**: VideoDriverKit  
**Kind**: class

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoSelectorControl;
```

#### Overview

IOUserVideoSelectorControl is a subclass of IOUserVideoControl

Control object that supports a uint32_t IOUserVideoSelectorValue

## Topics

### Creating a selector control
- [Create](iouservideoselectorcontrol/create.md)
- [init](iouservideoselectorcontrol/init.md)
- [IOUserVideoDriver](iouservideodriver.md)
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
### Freeing a selector control
- [free](iouservideoselectorcontrol/free.md)
### Getting information about the class
- [GetClassID](iouservideoselectorcontrol/getclassid.md)
- [GetBaseClassID](iouservideoselectorcontrol/getbaseclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
### Supporting value changes
- [HandleChangeSelectedValues](iouservideoselectorcontrol/handlechangeselectedvalues.md)
### Accessing the value
- [SetCurrentSelectedValues](iouservideoselectorcontrol/setcurrentselectedvalues.md)
- [GetCurrentSelectedValues](iouservideoselectorcontrol/getcurrentselectedvalues.md)
- [IOUserVideoSelectorValue](iouservideoselectorvalue.md)
- [GetControlValuesCount](iouservideoselectorcontrol/getcontrolvaluescount.md)
- [AddControlValueDescriptions](iouservideoselectorcontrol/addcontrolvaluedescriptions.md)
- [RemoveControlValueDescriptions](iouservideoselectorcontrol/removecontrolvaluedescriptions.md)
- [GetControlValueDescriptions](iouservideoselectorcontrol/getcontrolvaluedescriptions.md)
- [IOUserVideoSelectorValueDescription](iouservideoselectorvaluedescription.md)

## Relationships

### Inherits From
- [IOUserVideoControl](iouservideocontrol.md)

## See Also

- [IOUserVideoControl](iouservideocontrol.md)
- [IOUserVideoBooleanControl](iouservideobooleancontrol.md)
- [IOUserVideoStereoPanControl](iouservideostereopancontrol.md)
- [IOUserVideoSliderControl](iouservideoslidercontrol.md)
- [IOUserVideoDirectionControl](iouservideodirectioncontrol.md)
- [IOUserVideoLevelControl](iouservideolevelcontrol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol)*