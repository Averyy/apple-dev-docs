# GetCustomPropertyValueWithQualifier

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t GetCustomPropertyValueWithQualifier(OSObject *in_qualifier_data, OSObject **out_data);
```

#### Return Value

Returns kIOReturnSuccess on sucess.

#### Discussion

Get the custom property value for a given qualifier

Base class will return the custom property value set on the object without looking at contents of the qualifier data.  If the value returned is dependent on qualfier, IOUserVideoCustomProperty should be subclassed and derived class should override this method.

## Parameters

- `in_qualifier_data`: The OSObject that is used to qualify the custom property data value.  in_qualifier_data can be a nullptr if custom property value does not require qualifier data.
- `out_data`: Returned OSObject that is retained and to be released by the caller.

## See Also

- [SetQualifierAndDataValue](iouservideocustomproperty/setqualifieranddatavalue.md)
- [GetCustomPropertyInfo](iouservideocustomproperty/getcustompropertyinfo.md)
- [IOUserVideoCustomPropertyInfo](videodriverkit/iouservideocustompropertyinfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty/getcustompropertyvaluewithqualifier)*