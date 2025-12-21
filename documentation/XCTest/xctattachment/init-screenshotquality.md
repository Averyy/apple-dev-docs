# init(screenshot:quality:)

**Framework**: XCTest  
**Kind**: init

Creates an attachment containing a representation of the provided screenshot at the requested image quality.

## Declaration

```swift
convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"public.png"` when `quality` is [`XCTAttachment.ImageQuality.original`](xctattachment/imagequality/original.md), and a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"public.jpeg"` when `quality` is [`XCTAttachment.ImageQuality.medium`](xctattachment/imagequality/medium.md) or [`XCTAttachment.ImageQuality.low`](xctattachment/imagequality/low.md).

## Parameters

- `screenshot`: The screenshot to wrap as an attachment.
- `quality`: The quality setting to use when storing the screenshot in the attachment.

## See Also

- [convenience init(image: UIImage)](xctattachment/init(image:).md)
  Creates an attachment containing a PNG representation of the provided image.
- [convenience init(image: UIImage, quality: XCTAttachment.ImageQuality)](xctattachment/init(image:quality:).md)
  Creates an attachment containing a representation of the provided image at the requested image quality.
- [convenience init(screenshot: XCUIScreenshot)](xctattachment/init(screenshot:).md)
  Creates an attachment containing a PNG representation of the provided screenshot.
- [class XCUIScreenshot](../XCUIAutomation/XCUIScreenshot.md)
  A captured image of a screen, app, or UI element state.
- [XCTAttachment.ImageQuality](xctattachment/imagequality.md)
  Compression quality options for image-based attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(screenshot:quality:))*