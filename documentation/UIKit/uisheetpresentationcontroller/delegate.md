# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the sheet presentation controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UISheetPresentationControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UISheetPresentationControllerDelegate> delegate;
```

## See Also

### Managing the delegate
- [protocol UISheetPresentationControllerDelegate](../uisheetpresentationcontrollerdelegate.md)
  The interface that an object implements to respond to size changes in a sheet presentation controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/delegate)*