# setIsAccessibilityElement(_:)

**Framework**: Watchkit  
**Kind**: method

Sets whether the object is an accessibility element that an assistive app can access.

**Availability**:
- watchOS ?+

## Declaration

```swift
func setIsAccessibilityElement(_ isAccessibilityElement: Bool)
```

#### Discussion

Use this method to change the accessibility status of your interface objects.

## Parameters

- `isAccessibilityElement`:   if the object is an accessibility element or   if it is not.

## See Also

- [func setAccessibilityIdentifier(String?)](wkinterfaceobject/setaccessibilityidentifier(_:).md)
  Sets the unique identifier string for the interface object.
- [func setAccessibilityLabel(String?)](wkinterfaceobject/setaccessibilitylabel(_:).md)
  Sets a succinct label on the object that identifies the accessibility element.
- [func setAccessibilityHint(String?)](wkinterfaceobject/setaccessibilityhint(_:).md)
  Sets the description of what happens when performing an action on the accessibility element.
- [func setAccessibilityValue(String?)](wkinterfaceobject/setaccessibilityvalue(_:).md)
  Sets the value of the accessibility element.
- [func setAccessibilityTraits(UIAccessibilityTraits)](wkinterfaceobject/setaccessibilitytraits(_:).md)
  Sets the combination of accessibility traits that best characterize the accessibility element.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](wkinterfaceobject/setaccessibilityimageregions(_:).md)
  Marks portions of an image as separate accessible elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setisaccessibilityelement(_:))*