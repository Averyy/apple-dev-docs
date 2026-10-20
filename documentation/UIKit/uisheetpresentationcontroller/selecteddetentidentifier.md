# selectedDetentIdentifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The identifier of the most recently selected detent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var selectedDetentIdentifier: UISheetPresentationController.Detent.Identifier? { get set }
```

```objc
@property (nonatomic, copy, nullable) UISheetPresentationControllerDetentIdentifier selectedDetentIdentifier;
```

#### Discussion

This property represents the most recent detent that the user selects or that you set programmatically. The default value is `nil`, which means the sheet displays at the smallest detent you specify in [`detents`](./detents.md).

## See Also

### Specifying the height
- [var detents: [UISheetPresentationController.Detent]](./detents.md)
  The array of heights where a sheet can rest.
- [UISheetPresentationController.Detent](./detent.md)
  An object that represents a height where a sheet naturally rests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/selecteddetentidentifier)*