# GetElementNumberName

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<OSString> GetElementNumberName(IOUserVideoObjectPropertyElement in_element, IOUserVideoObjectPropertyScope in_scope);
```

#### Return Value

Returns an OSSharedPtr to an OSString

#### Discussion

Get the number name for the given element and scope of the IOUserVideoObject. Getting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_element`: The IOUserVideoObjectPropertyElement
- `in_scope`: The IOUserVideoObjectPropertyScope

## See Also

- [GetElementCategoryName](iouservideoobject/getelementcategoryname.md)
- [SetElementCategoryName](iouservideoobject/setelementcategoryname.md)
- [GetElementName](iouservideoobject/getelementname.md)
- [SetElementName](iouservideoobject/setelementname.md)
- [SetElementNumberName](iouservideoobject/setelementnumbername.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoobject/getelementnumbername)*