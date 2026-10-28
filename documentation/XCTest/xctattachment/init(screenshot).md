# init(screenshot:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment containing a PNG representation of the provided screenshot.

## Declaration

```swift
convenience init(screenshot: XCUIScreenshot)
```

```objc
+ (instancetype) attachmentWithScreenshot:(XCUIScreenshot *) screenshot;
```

## Discussion

Creates an attachment with a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"public.png"`. Equivalent to calling [`init(screenshot:quality:)`](./init%28screenshot,quality%29.md) with a `quality` value of [`XCTAttachment.ImageQuality.original`](./imagequality/original.md).

## Parameters

- `screenshot`: The screenshot to wrap as an attachment.

## See Also

### Creating Attachments from Images and Screenshots
- [convenience init(image: UIImage)](./init%28image%29.md)
  Creates an attachment containing a PNG representation of the provided image.
- [convenience init(image: UIImage, quality: XCTAttachment.ImageQuality)](./init%28image,quality%29.md)
  Creates an attachment containing a representation of the provided image at the requested image quality.
- [convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)](./init%28screenshot,quality%29.md)
  Creates an attachment containing a representation of the provided screenshot at the requested image quality.
- [class XCUIScreenshot](../../XCUIAutomation/xcuiscreenshot.md)
  A captured image of a screen, app, or UI element state.
- [XCTAttachment.ImageQuality](./imagequality.md)
  Compression quality options for image-based attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(screenshot:))*