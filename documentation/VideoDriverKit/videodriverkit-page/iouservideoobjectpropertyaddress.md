# IOUserVideoObjectPropertyAddress

**Framework**: VideoDriverKit  
**Kind**: struct  
**Role**: Structure

A data structure that contains all the three parts to identify a specific property, for easy transmission.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
struct IOUserVideoObjectPropertyAddress;
```

## Topics

### Address members
- [mSelector](./iouservideoobjectpropertyaddress/mselector.md)
  The selector for the property.
- [mScope](./iouservideoobjectpropertyaddress/mscope.md)
  The scope for the property.
- [mElement](./iouservideoobjectpropertyaddress/melement.md)
  The element for the property.

## See Also

### Working with custom properties
- [IOUserVideoCustomPropertyInfo](./iouservideocustompropertyinfo.md)
  A description of a a custom property that allow the Host to marshal the data between the Host and its clients.
- [IOUserVideoCustomPropertyDataType](./iouservideocustompropertydatatype.md)
  Data qualifier types used for custom properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideoobjectpropertyaddress)*