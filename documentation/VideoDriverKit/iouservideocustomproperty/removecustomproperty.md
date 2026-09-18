# RemoveCustomProperty

**Framework**: VideoDriverKit  
**Kind**: method

Always returns an error, because a custom property cannot have a custom property.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t RemoveCustomProperty(IOUserVideoCustomProperty *in_custom_property);
```

## See Also

- [AddCustomProperty](iouservideocustomproperty/addcustomproperty.md)
  Always returns `kIOReturnError` because a custom property cannot have a custom property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideocustomproperty/removecustomproperty)*