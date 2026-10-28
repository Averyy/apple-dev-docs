# effect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The visual effect provided by the view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var effect: UIVisualEffect? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIVisualEffect * effect;
```

## Discussion

The effect is either a [`UIBlurEffect`](../uiblureffect.md) or a [`UIVibrancyEffect`](../uivibrancyeffect.md).

## See Also

### Retrieving view information
- [var contentView: UIView](./contentview.md)
  A view object that can have a visual effect view added to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivisualeffectview/effect)*