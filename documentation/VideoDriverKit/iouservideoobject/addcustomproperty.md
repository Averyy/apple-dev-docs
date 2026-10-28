# AddCustomProperty

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Adds an custom property object to this object.

**Availability**:
- DriverKit 27.0+

## Declaration

```cpp
virtual kern_return_t AddCustomProperty(IOUserVideoCustomProperty *in_custom_property);
```

## Return Value

`kIOReturnSuccess` on success

## Parameters

- `in_custom_property`: A IOUserVideoCustomProperty object that should be added to the IOUserVideoObject

## See Also

### Using custom properties
- [RemoveCustomProperty](./removecustomproperty.md)
  Removes a custom property from the video object.
- [IOUserVideoCustomProperty](../iouservideocustomproperty.md)
  A custom property object that can be added to or associated with video objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/addcustomproperty)*