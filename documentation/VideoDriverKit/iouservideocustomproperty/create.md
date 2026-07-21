# Create

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
static OSSharedPtr<IOUserVideoCustomProperty> Create(IOUserVideoDriver *in_video_driver, IOUserVideoObjectPropertyAddress in_prop_addr, bool in_is_property_settable, IOUserVideoCustomPropertyDataType in_qualifier_data_type, IOUserVideoCustomPropertyDataType in_data_type);
```

#### Return Value

OSSharedPtr to an IOUserVideoBooleanControl if it was successfully allocated and initialized

#### Discussion

Static factory method to allocate and initialize an IOUserVideoCustomProperty.

If IOUserVideoCustomProperty is subclassed to override behavior, Create should not be used to allocate/initialize the custom subclass.

## Parameters

- `in_video_driver`: The IOUserVideoDriver that owns this object.
- `in_prop_addr`: The IOUserVideoObjectPropertyAddress of the custom property.
- `in_is_property_settable`: Bool value that indicates if the property can be set.
- `in_qualifier_data_type`: The IOUserVideoCustomPropertyDataType for custom property’s qualifier data value
- `in_data_type`: The IOUserVideoCustomPropertyDataType for custom property’s data value. Value cannot be IOUserVideoCustomPropertyDataType::None

## See Also

- [init](iouservideocustomproperty/init.md)
- [IOUserVideoObjectPropertyAddress](videodriverkit/iouservideoobjectpropertyaddress.md)
- [IOUserVideoCustomPropertyDataType](videodriverkit/iouservideocustompropertydatatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty/create)*