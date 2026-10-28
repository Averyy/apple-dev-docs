# setDecrementImage(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the image to use for the decrement glyph of the control.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setDecrementImage(_ image: UIImage?, for state: UIControl.State)
```

```objc
- (void) setDecrementImage:(UIImage *) image forState:(UIControlState) state;
```

## Discussion

The image you specify is used as a template image to create the final control. If you don’t specify a custom image, a minus (`-`) glyph is used.

## Parameters

- `image`: The image to use for the decrement glyph.
- `state`: The control state in which you want to display the image.

## See Also

### Customizing appearance
- [func backgroundImage(for: UIControl.State) -> UIImage?](./backgroundimage%28for%29.md)
  Returns the background image associated with the specified control state.
- [func setBackgroundImage(UIImage?, for: UIControl.State)](./setbackgroundimage%28_,for%29.md)
  Sets the background image for the control when it’s in the specified state.
- [func decrementImage(for: UIControl.State) -> UIImage?](./decrementimage%28for%29.md)
  Returns the image used for the decrement glyph of the control.
- [func dividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](./dividerimage%28forleftsegmentstate,rightsegmentstate%29.md)
  Returns the divider image for the given combination of left and right states.
- [func setDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](./setdividerimage%28_,forleftsegmentstate,rightsegmentstate%29.md)
  Sets the image to use for the given combination of left and right states.
- [func incrementImage(for: UIControl.State) -> UIImage?](./incrementimage%28for%29.md)
  Returns the image used for the increment glyph of the control.
- [func setIncrementImage(UIImage?, for: UIControl.State)](./setincrementimage%28_,for%29.md)
  Sets the image to use for the increment glyph of the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/setdecrementimage(_:for:))*