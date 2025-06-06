# setAccessibilityImageRegions(_:)

**Framework**: Watchkit  
**Kind**: method

Marks portions of an image as separate accessible elements.

**Availability**:
- watchOS ?+

## Declaration

```swift
func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])
```

#### Discussion

Use this method to associate different accessibility labels with different parts of the object’s image. You might also use this method to assign accessibility information to different parts of a dynamically generated image.

## Parameters

- `accessibilityImageRegions`: An array of   objects. Each object in the array represents a portion of the interface object’s foreground or background image that should be treated as a separate accessible element.

## See Also

- [func setAccessibilityIdentifier(String?)](wkinterfaceobject/setaccessibilityidentifier(_:).md)
  Sets the unique identifier string for the interface object.
- [func setAccessibilityLabel(String?)](wkinterfaceobject/setaccessibilitylabel(_:).md)
  Sets a succinct label on the object that identifies the accessibility element.
- [func setAccessibilityHint(String?)](wkinterfaceobject/setaccessibilityhint(_:).md)
  Sets the description of what happens when performing an action on the accessibility element.
- [func setAccessibilityValue(String?)](wkinterfaceobject/setaccessibilityvalue(_:).md)
  Sets the value of the accessibility element.
- [func setIsAccessibilityElement(Bool)](wkinterfaceobject/setisaccessibilityelement(_:).md)
  Sets whether the object is an accessibility element that an assistive app can access.
- [func setAccessibilityTraits(UIAccessibilityTraits)](wkinterfaceobject/setaccessibilitytraits(_:).md)
  Sets the combination of accessibility traits that best characterize the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:))*