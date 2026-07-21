# AddCustomProperty

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t AddCustomProperty(IOUserVideoCustomProperty *in_custom_property);
```

#### Return Value

Returns kIOReturnSuccess on success

#### Discussion

Adds a IOUserVideoCustomProperty object to this IOUserVideoObject.

## Parameters

- `in_custom_property`: A IOUserVideoCustomProperty object that should be added to the IOUserVideoObject

## See Also

- [RemoveCustomProperty](iouservideoobject/removecustomproperty.md)
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/addcustomproperty)*