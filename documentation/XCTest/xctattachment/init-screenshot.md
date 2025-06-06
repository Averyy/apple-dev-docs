# init(screenshot:)

**Framework**: Xctest  
**Kind**: init

Creates an attachment containing a PNG representation of the provided screenshot.

## Declaration

```swift
convenience init(screenshot: XCUIScreenshot)
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](xctattachment/uniformtypeidentifier.md) of `"public.png"`. Equivalent to calling [`init(screenshot:quality:)`](xctattachment/init(screenshot:quality:).md) with a `quality` value of [`XCTAttachment.ImageQuality.original`](xctattachment/imagequality/original.md).

## Parameters

- `screenshot`: The screenshot to wrap as an attachment.

## See Also

- [convenience init(image: UIImage)](xctattachment/init(image:).md)
  Creates an attachment containing a PNG representation of the provided image.
- [convenience init(image: UIImage, quality: XCTAttachment.ImageQuality)](xctattachment/init(image:quality:).md)
  Creates an attachment containing a representation of the provided image at the requested image quality.
- [convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)](xctattachment/init(screenshot:quality:).md)
  Creates an attachment containing a representation of the provided screenshot at the requested image quality.
- [@MainActor class XCUIScreenshot](../XCUIAutomation/XCUIScreenshot.md)
  A captured image of a screen, app, or UI element state.
- [XCTAttachment.ImageQuality](xctattachment/imagequality.md)
  Compression quality options for image-based attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(screenshot:))*