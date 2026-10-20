# init(screenshot:quality:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment containing a representation of the provided screenshot at the requested image quality.

## Declaration

```swift
convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)
```

```objc
+ (instancetype) attachmentWithScreenshot:(XCUIScreenshot *) screenshot quality:(XCTImageQuality) quality;
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"public.png"` when `quality` is [`XCTAttachment.ImageQuality.original`](./imagequality/original.md), and a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"public.jpeg"` when `quality` is [`XCTAttachment.ImageQuality.medium`](./imagequality/medium.md) or [`XCTAttachment.ImageQuality.low`](./imagequality/low.md).

## Parameters

- `screenshot`: The screenshot to wrap as an attachment.
- `quality`: The quality setting to use when storing the screenshot in the attachment.

## See Also

### Creating Attachments from Images and Screenshots
- [convenience init(image: UIImage)](./init%28image%29.md)
  Creates an attachment containing a PNG representation of the provided image.
- [convenience init(image: UIImage, quality: XCTAttachment.ImageQuality)](./init%28image,quality%29.md)
  Creates an attachment containing a representation of the provided image at the requested image quality.
- [convenience init(screenshot: XCUIScreenshot)](./init%28screenshot%29.md)
  Creates an attachment containing a PNG representation of the provided screenshot.
- [class XCUIScreenshot](../../XCUIAutomation/xcuiscreenshot.md)
  A captured image of a screen, app, or UI element state.
- [XCTAttachment.ImageQuality](./imagequality.md)
  Compression quality options for image-based attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(screenshot:quality:))*