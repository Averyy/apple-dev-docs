# RemoveCustomProperty

**Framework**: VideoDriverKit  
**Kind**: method

Removes a custom property from the video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t RemoveCustomProperty(IOUserVideoCustomProperty *in_custom_property);
```

#### Return Value

`kIOReturnSuccess` on success

## Parameters

- `in_custom_property`: A IOUserVideoCustomProperty object that should be removed from the IOUserVideoObject

## See Also

- [AddCustomProperty](iouservideoobject/addcustomproperty.md)
  Adds an custom property object to this object.
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)
  A custom property object that can be added to or associated with video objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/removecustomproperty)*