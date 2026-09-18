# IOUserVideoCustomProperty

**Framework**: VideoDriverKit  
**Kind**: class

A custom property object that can be added to or associated with video objects.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoCustomProperty;
```

#### Overview

Custom properties can be added to the following objects: [`IOUserVideoControl`](iouservideocontrol.md), [`IOUserVideoBox`](iouservideobox.md), [`IOUserVideoStream`](iouservideostream.md), [`IOUserVideoClockDevice`](iouservideoclockdevice.md), [`IOUserVideoDevice`](iouservideodevice.md), [`IOUserVideoDriver`](iouservideodriver.md). Custom properties have qualifier and data types of `OSString`, `OSDictionary`, or `OSData`.

## Topics

### Creating a custom property
- [Create](iouservideocustomproperty/create.md)
  A static factory method that allocates and initializes a custom property.
- [init](iouservideocustomproperty/init.md)
  Initializes a custom property.
- [IOUserVideoObjectPropertyAddress](videodriverkit/iouservideoobjectpropertyaddress.md)
  A data structure that contains all the three parts to identify a specific property, for easy transmission.
- [IOUserVideoCustomPropertyDataType](videodriverkit/iouservideocustompropertydatatype.md)
  Data qualifier types used for custom properties.
### Freeing a custom property
- [free](iouservideocustomproperty/free.md)
  Frees the custom property.
### Getting information about the class
- [GetClassID](iouservideocustomproperty/getclassid.md)
  Gets the class identifier of the object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Supporting data value changes
- [HandleChangeCustomPropertyDataValueWithQualifier](iouservideocustomproperty/handlechangecustompropertydatavaluewithqualifier.md)
  The system calls this virtual method when the custom property’s data value changes.
### Accessing the data value
- [SetQualifierAndDataValue](iouservideocustomproperty/setqualifieranddatavalue.md)
  Sets the custom property’s data value.
- [GetCustomPropertyValueWithQualifier](iouservideocustomproperty/getcustompropertyvaluewithqualifier.md)
  Gets the custom property value for a given qualifier.
- [GetCustomPropertyInfo](iouservideocustomproperty/getcustompropertyinfo.md)
  Gets the custom property information.
- [IOUserVideoCustomPropertyInfo](videodriverkit/iouservideocustompropertyinfo.md)
  A description of a a custom property that allow the Host to marshal the data between the Host and its clients.
### Working with custom properties
- [AddCustomProperty](iouservideocustomproperty/addcustomproperty.md)
  Always returns `kIOReturnError` because a custom property cannot have a custom property.
- [RemoveCustomProperty](iouservideocustomproperty/removecustomproperty.md)
  Always returns an error, because a custom property cannot have a custom property.

## Relationships

### Inherits From
- [IOUserVideoObject](iouservideoobject.md)

## See Also

- [AddCustomProperty](iouservideodriver/addcustomproperty.md)
  Adds a custom property object to the video driver.
- [RemoveCustomProperty](iouservideodriver/removecustomproperty.md)
  Removes a custom property object from the video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty)*