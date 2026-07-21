# RemoveCustomProperty

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t RemoveCustomProperty(IOUserVideoCustomProperty *in_custom_property);
```

#### Return Value

Returns kIOReturnError

#### Discussion

Will always return kIOReturnError since a custom property cannot have a custom property

## See Also

- [AddCustomProperty](iouservideocustomproperty/addcustomproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty/removecustomproperty)*