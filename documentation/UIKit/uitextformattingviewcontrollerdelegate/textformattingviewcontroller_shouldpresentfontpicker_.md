# textFormattingViewController:shouldPresentFontPicker:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

If implemented, text formatting will call this method before presenting font picker controller. Use this method to make any presentation modifications or to prevent presentation altogether.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 26.0+

## Declaration

```objc
- (BOOL) textFormattingViewController:(UITextFormattingViewController *) viewController shouldPresentFontPicker:(UIFontPickerViewController *) fontPicker;
```

## Return Value

Flag indicating if text formatting controller should present font picker.

## Discussion

If you decide to prevent presentation of font picker via text formatting controller, you may present provided font picker yourself. In this case, you will have to handle any font picker actions independently.

## Parameters

- `viewController`: Text formatting controller that is attempting to present font picker controller
- `fontPicker`: Font picker controller that will be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller:shouldpresentfontpicker:)*