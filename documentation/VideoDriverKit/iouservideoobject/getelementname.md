# GetElementName

**Framework**: VideoDriverKit  
**Kind**: method

Gets the name for the given element and scope of the video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
OSSharedPtr<OSString> GetElementName(IOUserVideoObjectPropertyElement in_element, IOUserVideoObjectPropertyScope in_scope);
```

#### Return Value

The element name.

#### Discussion

The object’s work queue synchronizes access to the value.

## Parameters

- `in_element`: The element.
- `in_scope`: The scope.

## See Also

- [GetElementCategoryName](iouservideoobject/getelementcategoryname.md)
  Gets the category name for the given element and scope of the video object.
- [SetElementCategoryName](iouservideoobject/setelementcategoryname.md)
  Sets the category name for the given element and scope of the video object.
- [SetElementName](iouservideoobject/setelementname.md)
  Sets the name for the given element and scope of the video object.
- [GetElementNumberName](iouservideoobject/getelementnumbername.md)
  Gets the number name for the given element and scope of the video object.
- [SetElementNumberName](iouservideoobject/setelementnumbername.md)
  Sets the number name for the given element of the video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/getelementname)*