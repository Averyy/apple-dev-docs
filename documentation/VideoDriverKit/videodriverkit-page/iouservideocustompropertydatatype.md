# IOUserVideoCustomPropertyDataType

**Framework**: VideoDriverKit  
**Kind**: enum  
**Role**: Enumeration

Data qualifier types used for custom properties.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
enum IOUserVideoCustomPropertyDataType : uint32_t;
```

## Topics

### Data types
- [Dictionary](./iouservideocustompropertydatatype/dictionary.md)
  The custom property data type is an `OSDictionary` value.
- [String](./iouservideocustompropertydatatype/string.md)
  The custom property data type is an `OSString` value.
- [None](./iouservideocustompropertydatatype/none.md)
  The custom property does not have any data.

## See Also

### Working with custom properties
- [IOUserVideoCustomPropertyInfo](./iouservideocustompropertyinfo.md)
  A description of a a custom property that allow the Host to marshal the data between the Host and its clients.
- [IOUserVideoObjectPropertyAddress](./iouservideoobjectpropertyaddress.md)
  A data structure that contains all the three parts to identify a specific property, for easy transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideocustompropertydatatype)*