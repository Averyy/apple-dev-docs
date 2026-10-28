# GetElementCategoryName

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the category name for the given element and scope of the video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
OSSharedPtr<OSString> GetElementCategoryName(IOUserVideoObjectPropertyElement in_element, IOUserVideoObjectPropertyScope in_scope);
```

## Return Value

The category name.

## Discussion

The object’s work queue synchronizes access to the value.

## Parameters

- `in_element`: The element.
- `in_scope`: The scope.

## See Also

### Working with elements
- [SetElementCategoryName](./setelementcategoryname.md)
  Sets the category name for the given element and scope of the video object.
- [GetElementName](./getelementname.md)
  Gets the name for the given element and scope of the video object.
- [SetElementName](./setelementname.md)
  Sets the name for the given element and scope of the video object.
- [GetElementNumberName](./getelementnumbername.md)
  Gets the number name for the given element and scope of the video object.
- [SetElementNumberName](./setelementnumbername.md)
  Sets the number name for the given element of the video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/getelementcategoryname)*