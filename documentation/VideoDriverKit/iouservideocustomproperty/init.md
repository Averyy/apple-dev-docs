# init

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_video_driver, IOUserVideoObjectPropertyAddress in_prop_addr, bool in_is_property_settable, IOUserVideoCustomPropertyDataType in_qualifier_data_type, IOUserVideoCustomPropertyDataType in_data_type);
```

#### Return Value

True on success.

#### Discussion

Initializes a IOUserVideoCustomProperty.

## Parameters

- `in_video_driver`: The IOUserVideoDriver that owns this object.
- `in_prop_addr`: The IOUserVideoObjectPropertyAddress of the custom property.
- `in_is_property_settable`: Bool value that indicates if the property can be set.
- `in_qualifier_data_type`: The IOUserVideoCustomPropertyDataType for custom property’s qualifier data value
- `in_data_type`: The IOUserVideoCustomPropertyDataType for custom property’s data value

## See Also

- [Create](iouservideocustomproperty/create.md)
- [IOUserVideoObjectPropertyAddress](videodriverkit/iouservideoobjectpropertyaddress.md)
- [IOUserVideoCustomPropertyDataType](videodriverkit/iouservideocustompropertydatatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty/init)*