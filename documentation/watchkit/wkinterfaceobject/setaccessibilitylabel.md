# setAccessibilityLabel(_:)

**Framework**: WatchKit  
**Kind**: method

Sets a succinct label on the object that identifies the accessibility element.

**Availability**:
- watchOS ?+

## Declaration

```swift
func setAccessibilityLabel(_ accessibilityLabel: String?)
```

#### Discussion

Use this method to change the accessibility label of an object dynamically. You can also set the accessibility label for an object in Xcode from the Identity inspector. If you do not set an accessibility label, the system uses the object’s title string, if present.

An assistive application uses this label to identify the item to a user with disabilities. For example, if a button uses an image to convey its meaning to sighted users, you can assign a label that describes the behavior of the button to users with disabilities.

## Parameters

- `accessibilityLabel`: A localized string for identifying the object to the accessibility system. The string you specify should succinctly describe the purpose of the object.

## See Also

- [func setAccessibilityIdentifier(String?)](setaccessibilityidentifier(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityidentifier(_:)))
  Sets the unique identifier string for the interface object.
- [func setAccessibilityHint(String?)](setaccessibilityhint(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityhint(_:)))
  Sets the description of what happens when performing an action on the accessibility element.
- [func setAccessibilityValue(String?)](setaccessibilityvalue(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityvalue(_:)))
  Sets the value of the accessibility element.
- [func setIsAccessibilityElement(Bool)](setisaccessibilityelement(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setisaccessibilityelement(_:)))
  Sets whether the object is an accessibility element that an assistive app can access.
- [func setAccessibilityTraits(UIAccessibilityTraits)](setaccessibilitytraits(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitytraits(_:)))
  Sets the combination of accessibility traits that best characterize the accessibility element.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](setaccessibilityimageregions(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:)))
  Marks portions of an image as separate accessible elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitylabel(_:))*