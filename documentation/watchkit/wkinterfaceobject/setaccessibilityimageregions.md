# setAccessibilityImageRegions(_:)

**Framework**: WatchKit  
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
- [func setAccessibilityTraits(UIAccessibilityTraits)](setaccessibilitytraits(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitytraits(_:)))
  Sets the combination of accessibility traits that best characterize the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:))*