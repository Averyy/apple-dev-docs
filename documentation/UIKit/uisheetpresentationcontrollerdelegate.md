# UISheetPresentationControllerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol UISheetPresentationControllerDelegate <UIAdaptivePresentationControllerDelegate>
```

## Topics

### Resizing the Sheet Presentation Controller
- [func sheetPresentationControllerDidChangeSelectedDetentIdentifier(UISheetPresentationController)](./uisheetpresentationcontrollerdelegate/sheetpresentationcontrollerdidchangeselecteddetentidentifier%28_%29.md)
  Provides an opportunity to respond after the sheet presentation controller’s selected detent changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIAdaptivePresentationControllerDelegate](./uiadaptivepresentationcontrollerdelegate.md)

## See Also

### Managing the delegate
- [var delegate: (any UISheetPresentationControllerDelegate)?](./uisheetpresentationcontroller/delegate.md)
  The delegate of the sheet presentation controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdelegate)*