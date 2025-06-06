# animateChanges(_:)

**Framework**: UIKit  
**Kind**: method

Animates the UI changes to the sheet’s properties.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func animateChanges(_ changes: () -> Void)
```

#### Discussion

To animate changes to any of the sheet’s properties, set them inside the block that you pass to this method. By the time this method returns, layout finishes for the sheet, all adjacent sheets in the sheet stack, and their subviews.

## Parameters

- `changes`: A block where you change the sheet’s properties to animate them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/animatechanges(_:))*