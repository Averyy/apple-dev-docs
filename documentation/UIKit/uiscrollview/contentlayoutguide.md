# contentLayoutGuide

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The layout guide based on the untranslated content rectangle of the scroll view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var contentLayoutGuide: UILayoutGuide { get }
```

```objc
@property (nonatomic, strong, readonly) UILayoutGuide * contentLayoutGuide;
```

#### Discussion

Use this layout guide when you want to create Auto Layout constraints related to the content area of a scroll view.

## See Also

### Getting the layout guides
- [var frameLayoutGuide: UILayoutGuide](./framelayoutguide.md)
  The layout guide based on the untransformed frame rectangle of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/contentlayoutguide)*