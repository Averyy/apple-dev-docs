# SetElementName

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the name for the given element and scope of the video object.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetElementName(IOUserVideoObjectPropertyElement in_element, IOUserVideoObjectPropertyScope in_scope, OSString *in_name);
```

## Return Value

A kern_return_t value indicating success or failure.

## Discussion

If the object can change the name dynamically, the object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to this value.

## Parameters

- `in_element`: The IOUserVideoObjectPropertyElement.
- `in_scope`: The IOUserVideoObjectPropertyScope.
- `in_name`: An OSString name to set.

## See Also

### Working with elements
- [GetElementCategoryName](./getelementcategoryname.md)
  Gets the category name for the given element and scope of the video object.
- [SetElementCategoryName](./setelementcategoryname.md)
  Sets the category name for the given element and scope of the video object.
- [GetElementName](./getelementname.md)
  Gets the name for the given element and scope of the video object.
- [GetElementNumberName](./getelementnumbername.md)
  Gets the number name for the given element and scope of the video object.
- [SetElementNumberName](./setelementnumbername.md)
  Sets the number name for the given element of the video object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/setelementname)*