# AddCustomProperty

**Framework**: VideoDriverKit  
**Kind**: method

Adds a custom property object to the video driver.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t AddCustomProperty(IOUserVideoCustomProperty *in_custom_property);
```

#### Return Value

`kIOReturnSuccess` on success

## Parameters

- `in_custom_property`: The custom property object being added.

## See Also

- [RemoveCustomProperty](iouservideodriver/removecustomproperty.md)
  Removes a custom property object from the video driver.
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)
  A custom property object that can be added to or associated with video objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/addcustomproperty)*