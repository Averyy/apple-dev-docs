# decrementImage(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the image used for the decrement glyph of the control.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func decrementImage(for state: UIControl.State) -> UIImage?
```

```objc
- (UIImage *) decrementImageForState:(UIControlState) state;
```

## Return Value

The image used for the decrement glyph of the control.

## Parameters

- `state`: The control state in which the image is displayed.

## See Also

### Customizing appearance
- [func backgroundImage(for: UIControl.State) -> UIImage?](./backgroundimage%28for%29.md)
  Returns the background image associated with the specified control state.
- [func setBackgroundImage(UIImage?, for: UIControl.State)](./setbackgroundimage%28_,for%29.md)
  Sets the background image for the control when it’s in the specified state.
- [func setDecrementImage(UIImage?, for: UIControl.State)](./setdecrementimage%28_,for%29.md)
  Sets the image to use for the decrement glyph of the control.
- [func dividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](./dividerimage%28forleftsegmentstate,rightsegmentstate%29.md)
  Returns the divider image for the given combination of left and right states.
- [func setDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](./setdividerimage%28_,forleftsegmentstate,rightsegmentstate%29.md)
  Sets the image to use for the given combination of left and right states.
- [func incrementImage(for: UIControl.State) -> UIImage?](./incrementimage%28for%29.md)
  Returns the image used for the increment glyph of the control.
- [func setIncrementImage(UIImage?, for: UIControl.State)](./setincrementimage%28_,for%29.md)
  Sets the image to use for the increment glyph of the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistepper/decrementimage(for:))*