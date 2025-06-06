# UISheetPresentationControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface that an object implements to respond to size changes in a sheet presentation controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UISheetPresentationControllerDelegate : UIAdaptivePresentationControllerDelegate
```

## Topics

### Resizing the Sheet Presentation Controller
- [func sheetPresentationControllerDidChangeSelectedDetentIdentifier(UISheetPresentationController)](uisheetpresentationcontrollerdelegate/sheetpresentationcontrollerdidchangeselecteddetentidentifier(_:).md)
  Provides an opportunity to respond after the sheet presentation controller’s selected detent changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)

## See Also

- [var delegate: (any UISheetPresentationControllerDelegate)?](uisheetpresentationcontroller/delegate.md)
  The delegate of the sheet presentation controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdelegate)*