# SetElementCategoryName

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetElementCategoryName(IOUserVideoObjectPropertyElement in_element, IOUserVideoObjectPropertyScope in_scope, OSString *in_category_name);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the category name for the given element and scope of the IOUserVideoObject

If object can change the name dynamically, a notification will be sent to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_element`: The IOUserVideoObjectPropertyElement
- `in_scope`: The IOUserVideoObjectPropertyScope
- `in_category_name`: OSString category name to set.

## See Also

- [GetElementCategoryName](iouservideoobject/getelementcategoryname.md)
- [GetElementName](iouservideoobject/getelementname.md)
- [SetElementName](iouservideoobject/setelementname.md)
- [GetElementNumberName](iouservideoobject/getelementnumbername.md)
- [SetElementNumberName](iouservideoobject/setelementnumbername.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/setelementcategoryname)*