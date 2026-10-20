# view

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view from which the view print formatter was derived.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var view: UIView { get }
```

```objc
@property (nonatomic, readonly) UIView * view;
```

#### Discussion

You obtain a view print formatter by calling [`viewPrintFormatter()`](../uiview/viewprintformatter%28%29.md) on a [`UIView`](../uiview.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewprintformatter/view)*