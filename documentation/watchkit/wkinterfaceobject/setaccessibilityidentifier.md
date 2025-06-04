# setAccessibilityIdentifier(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the unique identifier string for the interface object.

**Availability**:
- watchOS ?+

## Declaration

```swift
func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)
```

## Overview

Use the identifier in this property to distinguish between different objects in your app. The identifier string is used solely for programmatic identity, as opposed to many other accessibility attributes.

## Parameters

- `accessibilityIdentifier`: A string containing the identifier of the element. Specify   to clear the existing identifier.

## See Also

- [func setAccessibilityLabel(String?)](setaccessibilitylabel(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitylabel(_:)))
- [func setAccessibilityHint(String?)](setaccessibilityhint(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityhint(_:)))
- [func setAccessibilityValue(String?)](setaccessibilityvalue(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityvalue(_:)))
- [func setIsAccessibilityElement(Bool)](setisaccessibilityelement(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setisaccessibilityelement(_:)))
- [func setAccessibilityTraits(UIAccessibilityTraits)](setaccessibilitytraits(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitytraits(_:)))
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](setaccessibilityimageregions(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityidentifier(_:))*