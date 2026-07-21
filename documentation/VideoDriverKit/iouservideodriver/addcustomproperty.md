# AddCustomProperty

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t AddCustomProperty(IOUserVideoCustomProperty *in_custom_property);
```

#### Return Value

Returns kIOReturnSuccess on success

#### Discussion

Adds a IOUserVideoCustomProperty object to the IOUserVideoDriver.

## Parameters

- `in_custom_property`: A IOUserVideoCustomProperty object that should be added to the IOUserVideoDriver

## See Also

- [RemoveCustomProperty](iouservideodriver/removecustomproperty.md)
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/addcustomproperty)*