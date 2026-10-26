# textFormattingViewController:shouldPresentColorPicker:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

If implemented, text formatting will call this method before presenting color picker controller. Use this method to make any presentation modifications or to prevent presentation altogether.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 26.0+

## Declaration

```objc
- (BOOL) textFormattingViewController:(UITextFormattingViewController *) viewController shouldPresentColorPicker:(UIColorPickerViewController *) colorPicker;
```

#### Return Value

Flag indicating if text formatting controller should present font picker.

#### Discussion

You may decide to prevent presentation of color picker via text formatting controller. In that case, you may present provided color picker controller yourself, but you will have to handle any actions in that controller separately.

## Parameters

- `viewController`: Text formatting controller that is attempting to present font picker controller
- `colorPicker`: Color picker controller that will be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerdelegate/textformattingviewcontroller:shouldpresentcolorpicker:)*