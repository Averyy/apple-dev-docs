# init(image:quality:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment containing a representation of the provided image at the requested image quality.

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
convenience init(image: UIImage, quality: XCTAttachment.ImageQuality)
```

*macOS*

```swift
convenience init(image: NSImage, quality: XCTAttachment.ImageQuality)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
+ (instancetype) attachmentWithImage:(UIImage *) image quality:(XCTImageQuality) quality;
```

*macOS*

```objc
+ (instancetype) attachmentWithImage:(NSImage *) image quality:(XCTImageQuality) quality;
```

## Discussion

Creates an attachment with a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"public.png"` when `quality` is [`XCTAttachment.ImageQuality.original`](./imagequality/original.md), and a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"public.jpeg"` when `quality` is [`XCTAttachment.ImageQuality.medium`](./imagequality/medium.md) or [`XCTAttachment.ImageQuality.low`](./imagequality/low.md).

## Parameters

- `image`: The image to wrap as an attachment.
- `quality`: The quality setting to use when storing the image in the attachment.

## See Also

### Creating Attachments from Images and Screenshots
- [convenience init(image: UIImage)](./init%28image%29.md)
  Creates an attachment containing a PNG representation of the provided image.
- [convenience init(screenshot: XCUIScreenshot)](./init%28screenshot%29.md)
  Creates an attachment containing a PNG representation of the provided screenshot.
- [convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)](./init%28screenshot,quality%29.md)
  Creates an attachment containing a representation of the provided screenshot at the requested image quality.
- [class XCUIScreenshot](../../XCUIAutomation/xcuiscreenshot.md)
  A captured image of a screen, app, or UI element state.
- [XCTAttachment.ImageQuality](./imagequality.md)
  Compression quality options for image-based attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(image:quality:))*