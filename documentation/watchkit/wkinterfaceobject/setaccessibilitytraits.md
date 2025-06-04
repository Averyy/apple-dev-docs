# setAccessibilityTraits(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the combination of accessibility traits that best characterize the accessibility element.

**Availability**:
- watchOS ?+

## Declaration

```swift
func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)
```

#### Discussion

Use this method to change the accessibility traits associated with your interface objects.

## Parameters

- `accessibilityTraits`: The traits that characterize this element. For a list of traits and appropriate combinations, see  .

## See Also

- [func setAccessibilityIdentifier(String?)](setaccessibilityidentifier(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityidentifier(_:)))
  Sets the unique identifier string for the interface object.
- [func setAccessibilityLabel(String?)](setaccessibilitylabel(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitylabel(_:)))
  Sets a succinct label on the object that identifies the accessibility element.
- [func setAccessibilityHint(String?)](setaccessibilityhint(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityhint(_:)))
  Sets the description of what happens when performing an action on the accessibility element.
- [func setAccessibilityValue(String?)](setaccessibilityvalue(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityvalue(_:)))
  Sets the value of the accessibility element.
- [func setIsAccessibilityElement(Bool)](setisaccessibilityelement(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setisaccessibilityelement(_:)))
  Sets whether the object is an accessibility element that an assistive app can access.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](setaccessibilityimageregions(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:)))
  Marks portions of an image as separate accessible elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitytraits(_:))*