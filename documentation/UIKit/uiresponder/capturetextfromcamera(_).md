# captureTextFromCamera(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Starts scanning text using the device’s camera.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func captureTextFromCamera(_ sender: Any?)
```

```objc
- (void) captureTextFromCamera:(id) sender;
```

#### Discussion

To receive callbacks from the data scanner, the responder should conform to either the [`UIKeyInput`](../uikeyinput.md) or [`UITextInput`](../uitextinput.md) protocol. If it conforms to [`UIKeyInput`](../uikeyinput.md), the scanner calls the [`insertText:`](../../AppKit/nstextinput/inserttext_.md) protocol method. If it conforms to [`UITextInput`](../uitextinput.md), the scanner calls the [`setMarkedText(_:selectedRange:)`](../uitextinput/setmarkedtext%28_,selectedrange%29.md) and [`unmarkText()`](../uitextinput/unmarktext%28%29.md) protocol methods.

To determine whether the data scanner runs on the user’s device, pass [`captureTextFromCamera(_:)`](./capturetextfromcamera%28_%29.md) to the [`canPerformAction(_:withSender:)`](./canperformaction%28_,withsender%29.md) method.

## Parameters

- `sender`: The object that invokes this method.

## See Also

### Related Documentation
- [Scanning data with the camera](../../VisionKit/scanning-data-with-the-camera.md)
  Enable Live Text data scanning of text and codes that appear in the camera’s viewfinder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/capturetextfromcamera(_:))*