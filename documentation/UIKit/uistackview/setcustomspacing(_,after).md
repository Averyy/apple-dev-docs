# setCustomSpacing(_:after:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Applies custom spacing after the specified view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setCustomSpacing(_ spacing: CGFloat, after arrangedSubview: UIView)
```

```objc
- (void) setCustomSpacing:(CGFloat) spacing afterView:(UIView *) arrangedSubview;
```

## See Also

### Adding space between items
- [func customSpacing(after: UIView) -> CGFloat](./customspacing%28after%29.md)
  Returns the custom spacing after the specified view.
- [class let spacingUseDefault: CGFloat](./spacingusedefault.md)
  The default spacing for subviews within a stack view.
- [class let spacingUseSystem: CGFloat](./spacingusesystem.md)
  The system-defined spacing to the neighboring view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/setcustomspacing(_:after:))*