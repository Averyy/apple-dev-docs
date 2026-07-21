# SetElementName

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetElementName(IOUserVideoObjectPropertyElement in_element, IOUserVideoObjectPropertyScope in_scope, OSString *in_name);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the name for the given element and scope of the IOUserVideoObject

If object can change the name dynamically, a notification will be sent to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_element`: The IOUserVideoObjectPropertyElement
- `in_scope`: The IOUserVideoObjectPropertyScope
- `in_name`: OSString name to set.

## See Also

- [GetElementCategoryName](iouservideoobject/getelementcategoryname.md)
- [SetElementCategoryName](iouservideoobject/setelementcategoryname.md)
- [GetElementName](iouservideoobject/getelementname.md)
- [GetElementNumberName](iouservideoobject/getelementnumbername.md)
- [SetElementNumberName](iouservideoobject/setelementnumbername.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/setelementname)*