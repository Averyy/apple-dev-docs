# beginFloatingCursor(at:)

**Framework**: UIKit  
**Kind**: method

Tells the object when the gesture that the system uses to manipulate the cursor begins.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func beginFloatingCursor(at point: CGPoint)
```

#### Discussion

UIKit calls this method when the user begins to perform a two-finger pan gesture to pick up the cursor. You can use this method to update the visual state of your text view. For example, you might use this method to display custom visual feedback for cursor movements.

If you do not implement this method, UIKit provides visual feedback only when the selection changes.

## Parameters

- `point`: The point at which the gesture occurred in your view. This point is in the coordinate space of the view in the   property.

## See Also

- [func updateFloatingCursor(at: CGPoint)](uitextinput/updatefloatingcursor(at:).md)
  Tells the object that the floating cursor moved to a new location.
- [func endFloatingCursor()](uitextinput/endfloatingcursor.md)
  Tells the object when the gesture that the system uses to manipulate the cursor ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/beginfloatingcursor(at:))*