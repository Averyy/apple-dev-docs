# largestUndimmedDetentIdentifier

**Framework**: UIKit  
**Kind**: property

The largest detent that doesn’t dim the view underneath the sheet.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@MainActor
var largestUndimmedDetentIdentifier: UISheetPresentationController.Detent.Identifier? { get set }
```

#### Discussion

The default value is `nil`, which means the system adds a noninteractive dimming view underneath the sheet at all detents. Set this property to only add the dimming view at detents larger than the detent you specify. For example, set this property to [`medium`](uisheetpresentationcontroller/detent/identifier-swift.struct/medium.md) to add the dimming view at the [`large`](uisheetpresentationcontroller/detent/identifier-swift.struct/large.md) detent.

Without a dimming view, the undimmed area around the sheet responds to user interaction, allowing for a nonmodal experience. You can use this behavior for sheets with interactive content underneath them.

## See Also

- [var prefersScrollingExpandsWhenScrolledToEdge: Bool](uisheetpresentationcontroller/prefersscrollingexpandswhenscrolledtoedge.md)
  A Boolean value that determines whether scrolling expands the sheet to a larger detent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/largestundimmeddetentidentifier)*