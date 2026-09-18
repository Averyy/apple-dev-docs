# RemoveCustomProperty

**Framework**: VideoDriverKit  
**Kind**: method

Removes a custom property object from the video driver.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RemoveCustomProperty(IOUserVideoCustomProperty *in_custom_property);
```

#### Return Value

`kIOReturnSuccess` on success.

## Parameters

- `in_custom_property`: An IOUserVideoCustomProperty object to remove from the IOUserVideoDriver.

## See Also

- [AddCustomProperty](iouservideodriver/addcustomproperty.md)
  Adds a custom property object to the video driver.
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)
  A custom property object that can be added to or associated with video objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/removecustomproperty)*