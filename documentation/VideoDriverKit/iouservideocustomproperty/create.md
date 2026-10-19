# Create

**Framework**: VideoDriverKit  
**Kind**: method

A static factory method that allocates and initializes a custom property.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
static OSSharedPtr<IOUserVideoCustomProperty> Create(IOUserVideoDriver *in_video_driver, IOUserVideoObjectPropertyAddress in_prop_addr, bool in_is_property_settable, IOUserVideoCustomPropertyDataType in_qualifier_data_type, IOUserVideoCustomPropertyDataType in_data_type);
```

#### Return Value

OSSharedPtr to an IOUserVideoBooleanControl if it was successfully allocated and initialized

#### Discussion

If IOUserVideoCustomProperty is subclassed to override behavior, don’t use this method to allocate or initialize the custom subclass.

## Parameters

- `in_video_driver`: The IOUserVideoDriver that owns this object.
- `in_prop_addr`: The IOUserVideoObjectPropertyAddress of the custom property.
- `in_is_property_settable`: Bool value that indicates if the property can be set.
- `in_qualifier_data_type`: The IOUserVideoCustomPropertyDataType for custom property’s qualifier data value
- `in_data_type`: The IOUserVideoCustomPropertyDataType for custom property’s data value. Value cannot be IOUserVideoCustomPropertyDataType::None

## See Also

- [init](iouservideocustomproperty/init.md)
  Initializes a custom property.
- [IOUserVideoObjectPropertyAddress](videodriverkit/iouservideoobjectpropertyaddress.md)
  A data structure that contains all the three parts to identify a specific property, for easy transmission.
- [IOUserVideoCustomPropertyDataType](videodriverkit/iouservideocustompropertydatatype.md)
  Data qualifier types used for custom properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty/create)*