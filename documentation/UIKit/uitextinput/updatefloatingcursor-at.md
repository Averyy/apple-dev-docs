# updateFloatingCursor(at:)

**Framework**: UIKit  
**Kind**: method

Tells the object that the floating cursor moved to a new location.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func updateFloatingCursor(at point: CGPoint)
```

#### Discussion

UIKit calls this method when the touch location changes for the two-finger pan gesture used to move the cursor. You can use this method to update the visual state of your text view. For example, you might use this method to display custom visual feedback for cursor movements.This method may be called multiple times while the user’s fingers are moving, so your implementation should be fast. If you do not implement this method, UIKit provides visual feedback only when the selection changes.

## Parameters

- `point`: The new touch point in the underlying view. This point is in the coordinate space of the view in the   property.

## See Also

- [func beginFloatingCursor(at: CGPoint)](uitextinput/beginfloatingcursor(at:).md)
  Tells the object when the gesture that the system uses to manipulate the cursor begins.
- [func endFloatingCursor()](uitextinput/endfloatingcursor.md)
  Tells the object when the gesture that the system uses to manipulate the cursor ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/updatefloatingcursor(at:))*