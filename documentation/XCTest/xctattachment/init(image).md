# init(image:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an attachment containing a PNG representation of the provided image.

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
convenience init(image: UIImage)
```

*macOS*

```swift
convenience init(image: NSImage)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
+ (instancetype) attachmentWithImage:(UIImage *) image;
```

*macOS*

```objc
+ (instancetype) attachmentWithImage:(NSImage *) image;
```

#### Discussion

Creates an attachment with a [`uniformTypeIdentifier`](./uniformtypeidentifier.md) of `"public.png"`. Equivalent to calling [`init(image:quality:)`](./init%28image,quality%29.md) with a `quality` value of [`XCTAttachment.ImageQuality.original`](./imagequality/original.md).

## Parameters

- `image`: The image to wrap as an attachment.

## See Also

### Creating Attachments from Images and Screenshots
- [convenience init(image: UIImage, quality: XCTAttachment.ImageQuality)](./init%28image,quality%29.md)
  Creates an attachment containing a representation of the provided image at the requested image quality.
- [convenience init(screenshot: XCUIScreenshot)](./init%28screenshot%29.md)
  Creates an attachment containing a PNG representation of the provided screenshot.
- [convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)](./init%28screenshot,quality%29.md)
  Creates an attachment containing a representation of the provided screenshot at the requested image quality.
- [class XCUIScreenshot](../../XCUIAutomation/xcuiscreenshot.md)
  A captured image of a screen, app, or UI element state.
- [XCTAttachment.ImageQuality](./imagequality.md)
  Compression quality options for image-based attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/init(image:))*