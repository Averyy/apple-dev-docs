# IOUserVideoLevelControl

**Framework**: VideoDriverKit  
**Kind**: class

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoLevelControl;
```

#### Overview

IOUserVideoLevelControl is a subclass of IOUserVideoControl

Control object that supports a float value level.  Getting/Setting control values can be done with scalar or decibel level values.

## Topics

### Creating a level control
- [Create](iouservideolevelcontrol/create.md)
- [init](iouservideolevelcontrol/init.md)
- [IOUserVideoDriver](iouservideodriver.md)
- [IOUserVideoLevelControlRange](iouservideolevelcontrolrange.md)
- [IOUserVideoObjectPropertyElement](videodriverkit/iouservideoobjectpropertyelement.md)
- [IOUserVideoObjectPropertyScope](videodriverkit/iouservideoobjectpropertyscope.md)
### Freeing a level control
- [free](iouservideolevelcontrol/free.md)
### Getting information about the class
- [GetClassID](iouservideolevelcontrol/getclassid.md)
- [GetBaseClassID](iouservideolevelcontrol/getbaseclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
### Supporting value changes
- [HandleChangeDecibelValue](iouservideolevelcontrol/handlechangedecibelvalue.md)
- [HandleChangeScalarValue](iouservideolevelcontrol/handlechangescalarvalue.md)
### Accessing the value
- [SetScalarValue](iouservideolevelcontrol/setscalarvalue.md)
- [SetDecibelValue](iouservideolevelcontrol/setdecibelvalue.md)
- [GetScalarValue](iouservideolevelcontrol/getscalarvalue.md)
- [GetDecibelValue](iouservideolevelcontrol/getdecibelvalue.md)

## Relationships

### Inherits From
- [IOUserVideoControl](iouservideocontrol.md)

## See Also

- [IOUserVideoControl](iouservideocontrol.md)
- [IOUserVideoBooleanControl](iouservideobooleancontrol.md)
- [IOUserVideoStereoPanControl](iouservideostereopancontrol.md)
- [IOUserVideoSliderControl](iouservideoslidercontrol.md)
- [IOUserVideoDirectionControl](iouservideodirectioncontrol.md)
- [IOUserVideoSelectorControl](iouservideoselectorcontrol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol)*