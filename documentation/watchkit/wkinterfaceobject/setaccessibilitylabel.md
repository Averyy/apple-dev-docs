# setAccessibilityLabel(_:)

**Framework**: Watchkit  
**Kind**: method

Sets a succinct label on the object that identifies the accessibility element.

**Availability**:
- watchOS ?+

## Declaration

```swift
func setAccessibilityLabel(_ accessibilityLabel: String?)
```

## Overview

Use this method to change the accessibility label of an object dynamically. You can also set the accessibility label for an object in Xcode from the Identity inspector. If you do not set an accessibility label, the system uses the object’s title string, if present.

An assistive application uses this label to identify the item to a user with disabilities. For example, if a button uses an image to convey its meaning to sighted users, you can assign a label that describes the behavior of the button to users with disabilities.

## Parameters

- `accessibilityLabel`: A localized string for identifying the object to the accessibility system. The string you specify should succinctly describe the purpose of the object.

## See Also

- [func setAccessibilityIdentifier(String?)](setaccessibilityidentifier(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityidentifier(_:)))
- [func setAccessibilityHint(String?)](setaccessibilityhint(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityhint(_:)))
- [func setAccessibilityValue(String?)](setaccessibilityvalue(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityvalue(_:)))
- [func setIsAccessibilityElement(Bool)](setisaccessibilityelement(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setisaccessibilityelement(_:)))
- [func setAccessibilityTraits(UIAccessibilityTraits)](setaccessibilitytraits(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitytraits(_:)))
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](setaccessibilityimageregions(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitylabel(_:))*