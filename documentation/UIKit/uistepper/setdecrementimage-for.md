# setDecrementImage(_:for:)

**Framework**: UIKit  
**Kind**: method

Sets the image to use for the decrement glyph of the control.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setDecrementImage(_ image: UIImage?, for state: UIControl.State)
```

#### Discussion

The image you specify is used as a template image to create the final control. If you don’t specify a custom image, a minus (`-`) glyph is used.

## Parameters

- `image`: The image to use for the decrement glyph.
- `state`: The control state in which you want to display the image.

## See Also

- [func backgroundImage(for: UIControl.State) -> UIImage?](uistepper/backgroundimage(for:).md)
  Returns the background image associated with the specified control state.
- [func setBackgroundImage(UIImage?, for: UIControl.State)](uistepper/setbackgroundimage(_:for:).md)
  Sets the background image for the control when it’s in the specified state.
- [func decrementImage(for: UIControl.State) -> UIImage?](uistepper/decrementimage(for:).md)
  Returns the image used for the decrement glyph of the control.
- [func dividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](uistepper/dividerimage(forleftsegmentstate:rightsegmentstate:).md)
  Returns the divider image for the given combination of left and right states.
- [func setDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](uistepper/setdividerimage(_:forleftsegmentstate:rightsegmentstate:).md)
  Sets the image to use for the given combination of left and right states.
- [func incrementImage(for: UIControl.State) -> UIImage?](uistepper/incrementimage(for:).md)
  Returns the image used for the increment glyph of the control.
- [func setIncrementImage(UIImage?, for: UIControl.State)](uistepper/setincrementimage(_:for:).md)
  Sets the image to use for the increment glyph of the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/setdecrementimage(_:for:))*