# IOUserVideoCustomProperty

**Framework**: VideoDriverKit  
**Kind**: class

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoCustomProperty;
```

#### Overview

Custom property object that can be added/associated to IOUserVideo objects.

Custom properties can be added to the following objects: IOUserVideoControl, IOUserVideoBox, IOUserVideoStream, IOUserVideoClockDevice, IOUserVideoDevice, IOUserVideoDriver. Custom properites have qualifier and data types of OSString, OSDictionary, or OSData.

## Topics

### Creating a custom property
- [Create](iouservideocustomproperty/create.md)
- [init](iouservideocustomproperty/init.md)
- [IOUserVideoObjectPropertyAddress](videodriverkit/iouservideoobjectpropertyaddress.md)
- [IOUserVideoCustomPropertyDataType](videodriverkit/iouservideocustompropertydatatype.md)
### Freeing a custom property
- [free](iouservideocustomproperty/free.md)
### Getting information about the class
- [GetClassID](iouservideocustomproperty/getclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
### Supporting data value changes
- [HandleChangeCustomPropertyDataValueWithQualifier](iouservideocustomproperty/handlechangecustompropertydatavaluewithqualifier.md)
### Accessing the data value
- [SetQualifierAndDataValue](iouservideocustomproperty/setqualifieranddatavalue.md)
- [GetCustomPropertyValueWithQualifier](iouservideocustomproperty/getcustompropertyvaluewithqualifier.md)
- [GetCustomPropertyInfo](iouservideocustomproperty/getcustompropertyinfo.md)
- [IOUserVideoCustomPropertyInfo](videodriverkit/iouservideocustompropertyinfo.md)
### Working with custom properties
- [AddCustomProperty](iouservideocustomproperty/addcustomproperty.md)
- [RemoveCustomProperty](iouservideocustomproperty/removecustomproperty.md)

## Relationships

### Inherits From
- [IOUserVideoObject](iouservideoobject.md)

## See Also

- [AddCustomProperty](iouservideodriver/addcustomproperty.md)
- [RemoveCustomProperty](iouservideodriver/removecustomproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty)*