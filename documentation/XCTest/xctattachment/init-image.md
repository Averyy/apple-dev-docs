# init(image:)

**Framework**: XCTest  
**Kind**: init

Creates an attachment containing a PNG representation of the provided image.

## Declaration

```swift
convenience init(image: UIImage)
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"public.png"`. Equivalent to calling [`init(image:quality:)`](xctattachment/init(image:quality:).md) with a `quality` value of [`XCTAttachment.ImageQuality.original`](xctattachment/imagequality/original.md).

## Parameters

- `image`: The image to wrap as an attachment.

## See Also

- [convenience init(image: UIImage, quality: XCTAttachment.ImageQuality)](xctattachment/init(image:quality:).md)
  Creates an attachment containing a representation of the provided image at the requested image quality.
- [convenience init(screenshot: XCUIScreenshot)](xctattachment/init(screenshot:).md)
  Creates an attachment containing a PNG representation of the provided screenshot.
- [convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)](xctattachment/init(screenshot:quality:).md)
  Creates an attachment containing a representation of the provided screenshot at the requested image quality.
- [@MainActor class XCUIScreenshot](../XCUIAutomation/XCUIScreenshot.md)
  A captured image of a screen, app, or UI element state.
- [XCTAttachment.ImageQuality](xctattachment/imagequality.md)
  Compression quality options for image-based attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(image:))*