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

## Overview

Use this method to associate different accessibility labels with different parts of the object’s image. You might also use this method to assign accessibility information to different parts of a dynamically generated image.

## Parameters

- `accessibilityImageRegions`: An array of   objects. Each object in the array represents a portion of the interface object’s foreground or background image that should be treated as a separate accessible element.

## See Also

- [func setAccessibilityIdentifier(String?)](setaccessibilityidentifier(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityidentifier(_:)))
- [func setAccessibilityLabel(String?)](setaccessibilitylabel(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitylabel(_:)))
- [func setAccessibilityHint(String?)](setaccessibilityhint(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityhint(_:)))
- [func setAccessibilityValue(String?)](setaccessibilityvalue(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityvalue(_:)))
- [func setIsAccessibilityElement(Bool)](setisaccessibilityelement(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setisaccessibilityelement(_:)))
- [func setAccessibilityTraits(UIAccessibilityTraits)](setaccessibilitytraits(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitytraits(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:))*