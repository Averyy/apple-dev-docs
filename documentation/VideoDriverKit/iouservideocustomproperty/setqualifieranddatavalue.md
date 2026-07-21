# SetQualifierAndDataValue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetQualifierAndDataValue(OSObject *in_qualifier_data, OSObject *in_data);
```

#### Return Value

Returns kIOReturnSuccess on sucess.

#### Discussion

Set the custom propertie’s data value.

## Parameters

- `in_qualifier_data`: The qualifier data OSObject for the custom property that corresponds to the data value. Must be nullptr if qualifier data type is CustomPropertyDataTypeNone. Must be an OSString if qualifier data type is CustomPropertyDataTypeOSString. Must be an OSDictionary if qualifier data type is CustomPropertyDataTypeOSDictionary.
- `in_data`: The data OSObject for the custom property that corresponds to the qualifier. Must be an OSString if data type is CustomPropertyDataTypeOSString. Must be an OSDictionary if data type is CustomPropertyDataTypeOSDictionary. Value cannot be a nullptr.

## See Also

- [GetCustomPropertyValueWithQualifier](iouservideocustomproperty/getcustompropertyvaluewithqualifier.md)
- [GetCustomPropertyInfo](iouservideocustomproperty/getcustompropertyinfo.md)
- [IOUserVideoCustomPropertyInfo](videodriverkit/iouservideocustompropertyinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty/setqualifieranddatavalue)*