# detents

**Framework**: UIKit  
**Kind**: property

The array of heights where a sheet can rest.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@MainActor
var detents: [UISheetPresentationController.Detent] { get set }
```

#### Discussion

The default value is an array that contains the value [`large()`](uisheetpresentationcontroller/detent/large().md). This array must contain at least one element. When you set this value, specify detents in order from smallest to largest height.

## See Also

- [var selectedDetentIdentifier: UISheetPresentationController.Detent.Identifier?](uisheetpresentationcontroller/selecteddetentidentifier.md)
  The identifier of the most recently selected detent.
- [UISheetPresentationController.Detent](uisheetpresentationcontroller/detent.md)
  An object that represents a height where a sheet naturally rests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detents)*