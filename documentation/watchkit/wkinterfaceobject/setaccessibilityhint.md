# setAccessibilityHint(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the description of what happens when performing an action on the accessibility element.

**Availability**:
- watchOS ?+

## Declaration

```swift
func setAccessibilityHint(_ accessibilityHint: String?)
```

## Overview

Use this method to change the accessibility hint of an object dynamically. You can also set the accessibility hint for an object in Xcode from the Identity inspector.

Follow these guidelines to create a hint for interface objects:

- A hint should be a very brief phrase that begins with a verb that names the result of the action, such as “Dismisses the interface.” To avoid making the hint sound like a command, do not begin the phrase with the imperative form of a verb. For example, do not set the hint to “Dismiss the interface.”
- Do not repeat the action type in the hint. For example, do not create a hint such as “Tap to dismiss the interface.”
- Do not include information about the object involved in the hint. For example, do not create a hint such as “Row that displays details about the item.”

## Parameters

- `accessibilityHint`: A localized string describing what will happen when the user interacts with the object.

## See Also

- [func setAccessibilityIdentifier(String?)](setaccessibilityidentifier(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityidentifier(_:)))
- [func setAccessibilityLabel(String?)](setaccessibilitylabel(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitylabel(_:)))
- [func setAccessibilityValue(String?)](setaccessibilityvalue(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityvalue(_:)))
- [func setIsAccessibilityElement(Bool)](setisaccessibilityelement(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setisaccessibilityelement(_:)))
- [func setAccessibilityTraits(UIAccessibilityTraits)](setaccessibilitytraits(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitytraits(_:)))
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](setaccessibilityimageregions(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityhint(_:))*