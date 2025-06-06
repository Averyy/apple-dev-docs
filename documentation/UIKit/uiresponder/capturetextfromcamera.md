# captureTextFromCamera(_:)

**Framework**: UIKit  
**Kind**: method

Starts scanning text using the device’s camera.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func captureTextFromCamera(_ sender: Any?)
```

#### Discussion

To receive callbacks from the data scanner, the responder should conform to either the [`UIKeyInput`](uikeyinput.md) or [`UITextInput`](uitextinput.md) protocol. If it conforms to [`UIKeyInput`](uikeyinput.md), the scanner calls the [`insertText:`](https://developer.apple.com/documentation/AppKit/NSTextInput/insertText:) protocol method. If it conforms to [`UITextInput`](uitextinput.md), the scanner calls the [`setMarkedText(_:selectedRange:)`](uitextinput/setmarkedtext(_:selectedrange:).md) and [`unmarkText()`](uitextinput/unmarktext().md) protocol methods.

To determine whether the data scanner runs on the user’s device, pass [`captureTextFromCamera(_:)`](uiresponder/capturetextfromcamera(_:).md) to the [`canPerformAction(_:withSender:)`](uiresponder/canperformaction(_:withsender:).md) method.

## Parameters

- `sender`: The object that invokes this method.

## See Also

- [Scanning data with the camera](../VisionKit/scanning-data-with-the-camera.md)
  Enable Live Text data scanning of text and codes that appear in the camera’s viewfinder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/capturetextfromcamera(_:))*