# setAccessibilityValue(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the value of the accessibility element.

**Availability**:
- watchOS ?+

## Declaration

```swift
func setAccessibilityValue(_ accessibilityValue: String?)
```

#### Discussion

When an object has a static label and a dynamic value, set this property to a string that describes the value. For example, a switch object can have a label describing the meaning of the switch, but the value is either On or Off.

## Parameters

- `accessibilityValue`: The new value for the accessibility element.

## See Also

- [func setAccessibilityIdentifier(String?)](wkinterfaceobject/setaccessibilityidentifier(_:).md)
  Sets the unique identifier string for the interface object.
- [func setAccessibilityLabel(String?)](wkinterfaceobject/setaccessibilitylabel(_:).md)
  Sets a succinct label on the object that identifies the accessibility element.
- [func setAccessibilityHint(String?)](wkinterfaceobject/setaccessibilityhint(_:).md)
  Sets the description of what happens when performing an action on the accessibility element.
- [func setIsAccessibilityElement(Bool)](wkinterfaceobject/setisaccessibilityelement(_:).md)
  Sets whether the object is an accessibility element that an assistive app can access.
- [func setAccessibilityTraits(UIAccessibilityTraits)](wkinterfaceobject/setaccessibilitytraits(_:).md)
  Sets the combination of accessibility traits that best characterize the accessibility element.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](wkinterfaceobject/setaccessibilityimageregions(_:).md)
  Marks portions of an image as separate accessible elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityvalue(_:))*