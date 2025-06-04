# setAccessibilityHint(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the description of what happens when performing an action on the accessibility element.

**Availability**:
- watchOS ?+

## Declaration

```swift
func setAccessibilityHint(_ accessibilityHint: String?)
```

#### Discussion

Use this method to change the accessibility hint of an object dynamically. You can also set the accessibility hint for an object in Xcode from the Identity inspector.

Follow these guidelines to create a hint for interface objects:

- A hint should be a very brief phrase that begins with a verb that names the result of the action, such as “Dismisses the interface.” To avoid making the hint sound like a command, do not begin the phrase with the imperative form of a verb. For example, do not set the hint to “Dismiss the interface.”
- Do not repeat the action type in the hint. For example, do not create a hint such as “Tap to dismiss the interface.”
- Do not include information about the object involved in the hint. For example, do not create a hint such as “Row that displays details about the item.”

## Parameters

- `accessibilityHint`: A localized string describing what will happen when the user interacts with the object.

## See Also

- [func setAccessibilityIdentifier(String?)](wkinterfaceobject/setaccessibilityidentifier(_:).md)
  Sets the unique identifier string for the interface object.
- [func setAccessibilityLabel(String?)](wkinterfaceobject/setaccessibilitylabel(_:).md)
  Sets a succinct label on the object that identifies the accessibility element.
- [func setAccessibilityValue(String?)](wkinterfaceobject/setaccessibilityvalue(_:).md)
  Sets the value of the accessibility element.
- [func setIsAccessibilityElement(Bool)](wkinterfaceobject/setisaccessibilityelement(_:).md)
  Sets whether the object is an accessibility element that an assistive app can access.
- [func setAccessibilityTraits(UIAccessibilityTraits)](wkinterfaceobject/setaccessibilitytraits(_:).md)
  Sets the combination of accessibility traits that best characterize the accessibility element.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](wkinterfaceobject/setaccessibilityimageregions(_:).md)
  Marks portions of an image as separate accessible elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityhint(_:))*