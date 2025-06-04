# setAccessibilityValue(_:)

**Framework**: WatchKit  
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

- [func setAccessibilityIdentifier(String?)](setaccessibilityidentifier(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityidentifier(_:)))
  Sets the unique identifier string for the interface object.
- [func setAccessibilityLabel(String?)](setaccessibilitylabel(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitylabel(_:)))
  Sets a succinct label on the object that identifies the accessibility element.
- [func setAccessibilityHint(String?)](setaccessibilityhint(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityhint(_:)))
  Sets the description of what happens when performing an action on the accessibility element.
- [func setIsAccessibilityElement(Bool)](setisaccessibilityelement(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setisaccessibilityelement(_:)))
  Sets whether the object is an accessibility element that an assistive app can access.
- [func setAccessibilityTraits(UIAccessibilityTraits)](setaccessibilitytraits(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitytraits(_:)))
  Sets the combination of accessibility traits that best characterize the accessibility element.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](setaccessibilityimageregions(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:)))
  Marks portions of an image as separate accessible elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityvalue(_:))*