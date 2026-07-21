# HandleChangeCustomPropertyDataValueWithQualifier

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeCustomPropertyDataValueWithQualifier(OSObject *in_qualifier_data, OSObject *in_data);
```

#### Return Value

Returns kIOReturnSuccess on sucess. Upon sucess the custom property’s data value should be updated.

#### Discussion

Virtual Method will be called when the custom property’s data value will be changed.

Default implementation will always return kIOReturnSuccess and update the custom property data value without checking qualifier contents. Subclass and override this method to handle changes to this custom property value and return kIOReturnSucess upon success.

## Parameters

- `in_qualifier_data`: The qualifier data OSObject associated with setting the property data value. Can be a nullptr, OSString, or OSDictionary.
- `in_data`: The data OSObject that is getting set for the custom property. Can be a OSString or OSDictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty/handlechangecustompropertydatavaluewithqualifier)*