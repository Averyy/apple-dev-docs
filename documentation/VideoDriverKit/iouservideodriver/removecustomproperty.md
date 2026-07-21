# RemoveCustomProperty

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RemoveCustomProperty(IOUserVideoCustomProperty *in_custom_property);
```

#### Return Value

Returns kIOReturnSuccess on success

#### Discussion

Removes a IOUserVideoCustomProperty object that was previously added to the IOUserVideoDriver.

## Parameters

- `in_custom_property`: A IOUserVideoCustomProperty object that should be removed from the IOUserVideoDriver

## See Also

- [AddCustomProperty](iouservideodriver/addcustomproperty.md)
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/removecustomproperty)*