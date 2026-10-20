# contentView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A view object that can have a visual effect view added to it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var contentView: UIView { get }
```

```objc
@property (nonatomic, strong, readonly) UIView * contentView;
```

#### Discussion

Add subviews to the [`contentView`](./contentview.md) and not to [`UIVisualEffectView`](../uivisualeffectview.md) directly.

## See Also

### Retrieving view information
- [var effect: UIVisualEffect?](./effect.md)
  The visual effect provided by the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivisualeffectview/contentview)*