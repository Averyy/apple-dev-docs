# UITextFormattingViewControllerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 26.0+

## Declaration

```objc
@protocol UITextFormattingViewControllerDelegate <NSObject>
```

## Topics

### Instance Methods
- [- textFormattingDidFinish:](./uitextformattingviewcontrollerdelegate/textformattingdidfinish_.md)
  Informs the delegate that user has dismissed text formatting view controller.
- [- textFormattingViewController:didChangeValue:](./uitextformattingviewcontrollerdelegate/textformattingviewcontroller_didchangevalue_.md)
  Delegate method that will be invoked on any text formatting changes.
- [- textFormattingViewController:shouldPresentColorPicker:](./uitextformattingviewcontrollerdelegate/textformattingviewcontroller_shouldpresentcolorpicker_.md)
  If implemented, text formatting will call this method before presenting color picker controller. Use this method to make any presentation modifications or to prevent presentation altogether.
- [- textFormattingViewController:shouldPresentFontPicker:](./uitextformattingviewcontrollerdelegate/textformattingviewcontroller_shouldpresentfontpicker_.md)
  If implemented, text formatting will call this method before presenting font picker controller. Use this method to make any presentation modifications or to prevent presentation altogether.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerdelegate)*