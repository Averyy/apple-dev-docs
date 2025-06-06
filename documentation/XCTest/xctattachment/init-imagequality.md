# init(image:quality:)

**Framework**: Xctest  
**Kind**: init

Creates an attachment containing a representation of the provided image at the requested image quality.

## Declaration

```swift
convenience init(image: NSImage, quality: XCTAttachment.ImageQuality)
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"public.png"` when `quality` is [`XCTAttachment.ImageQuality.original`](xctattachment/imagequality/original.md), and a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"public.jpeg"` when `quality` is [`XCTAttachment.ImageQuality.medium`](xctattachment/imagequality/medium.md) or [`XCTAttachment.ImageQuality.low`](xctattachment/imagequality/low.md).

## Parameters

- `image`: The image to wrap as an attachment.
- `quality`: The quality setting to use when storing the image in the attachment.

## See Also

- [convenience init(image: UIImage)](xctattachment/init(image:).md)
  Creates an attachment containing a PNG representation of the provided image.
- [convenience init(screenshot: XCUIScreenshot)](xctattachment/init(screenshot:).md)
  Creates an attachment containing a PNG representation of the provided screenshot.
- [convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)](xctattachment/init(screenshot:quality:).md)
  Creates an attachment containing a representation of the provided screenshot at the requested image quality.
- [@MainActor class XCUIScreenshot](../XCUIAutomation/XCUIScreenshot.md)
  A captured image of a screen, app, or UI element state.
- [XCTAttachment.ImageQuality](xctattachment/imagequality.md)
  Compression quality options for image-based attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(image:quality:))*