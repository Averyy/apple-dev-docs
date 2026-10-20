# prefersScrollingExpandsWhenScrolledToEdge

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether scrolling expands the sheet to a larger detent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var prefersScrollingExpandsWhenScrolledToEdge: Bool { get set }
```

```objc
@property (nonatomic) BOOL prefersScrollingExpandsWhenScrolledToEdge;
```

#### Discussion

The default value is [`true`](../../Swift/true.md), which means if the sheet can expand to a larger detent than [`selectedDetentIdentifier`](./selecteddetentidentifier.md), scrolling up in the sheet increases its detent instead of scrolling the sheet’s content. After the sheet reaches its largest detent, scrolling begins.

Set this value to [`false`](../../Swift/false.md) if you want to avoid letting a scroll gesture expand the sheet. For example, you can set this value on a nonmodal sheet to avoid obscuring the content underneath the sheet.

## See Also

### Managing user interaction
- [var largestUndimmedDetentIdentifier: UISheetPresentationController.Detent.Identifier?](./largestundimmeddetentidentifier.md)
  The largest detent that doesn’t dim the view underneath the sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/prefersscrollingexpandswhenscrolledtoedge)*