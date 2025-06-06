# sheetPresentationControllerDidChangeSelectedDetentIdentifier(_:)

**Framework**: UIKit  
**Kind**: method

Provides an opportunity to respond after the sheet presentation controller’s selected detent changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@MainActor
optional func sheetPresentationControllerDidChangeSelectedDetentIdentifier(_ sheetPresentationController: UISheetPresentationController)
```

#### Discussion

Implement this method if you want to perform changes in response to the user resizing a sheet to a new detent.

The system calls this method after a sheet’s [`selectedDetentIdentifier`](uisheetpresentationcontroller/selecteddetentidentifier.md) changes in response to user interaction. The system doesn’t call this after you change [`selectedDetentIdentifier`](uisheetpresentationcontroller/selecteddetentidentifier.md) programmatically.

## Parameters

- `sheetPresentationController`: The sheet presentation controller whose detent changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdelegate/sheetpresentationcontrollerdidchangeselecteddetentidentifier(_:))*