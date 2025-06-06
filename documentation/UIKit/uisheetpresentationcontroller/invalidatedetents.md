# invalidateDetents()

**Framework**: UIKit  
**Kind**: method

Notifies the sheet to re-evaluate its detent value in the next layout pass.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
func invalidateDetents()
```

#### Discussion

When an external input (like a captured property) to a custom detent changes, call this method to notify the sheet to re-evaluate the detent.

To animate custom detents to their new heights, call this method within [`animateChanges(_:)`](uisheetpresentationcontroller/animatechanges(_:).md).

> **Note**:  You don’t need to call this method if [`detents`](uisheetpresentationcontroller/detents.md) only contains system detents, or if your custom detents only use information from the passed-in context.

 You don’t need to call this method if [`detents`](uisheetpresentationcontroller/detents.md) only contains system detents, or if your custom detents only use information from the passed-in context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/invalidatedetents())*