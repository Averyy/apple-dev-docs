# decrementImage(for:)

**Framework**: UIKit  
**Kind**: method

Returns the image used for the decrement glyph of the control.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func decrementImage(for state: UIControl.State) -> UIImage?
```

#### Return Value

The image used for the decrement glyph of the control.

## Parameters

- `state`: The control state in which the image is displayed.

## See Also

- [func backgroundImage(for: UIControl.State) -> UIImage?](uistepper/backgroundimage(for:).md)
  Returns the background image associated with the specified control state.
- [func setBackgroundImage(UIImage?, for: UIControl.State)](uistepper/setbackgroundimage(_:for:).md)
  Sets the background image for the control when it’s in the specified state.
- [func setDecrementImage(UIImage?, for: UIControl.State)](uistepper/setdecrementimage(_:for:).md)
  Sets the image to use for the decrement glyph of the control.
- [func dividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](uistepper/dividerimage(forleftsegmentstate:rightsegmentstate:).md)
  Returns the divider image for the given combination of left and right states.
- [func setDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](uistepper/setdividerimage(_:forleftsegmentstate:rightsegmentstate:).md)
  Sets the image to use for the given combination of left and right states.
- [func incrementImage(for: UIControl.State) -> UIImage?](uistepper/incrementimage(for:).md)
  Returns the image used for the increment glyph of the control.
- [func setIncrementImage(UIImage?, for: UIControl.State)](uistepper/setincrementimage(_:for:).md)
  Sets the image to use for the increment glyph of the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/decrementimage(for:))*