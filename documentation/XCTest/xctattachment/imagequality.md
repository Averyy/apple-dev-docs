# XCTAttachment.ImageQuality

**Framework**: XCTest  
**Kind**: enum

Compression quality options for image-based attachments.

## Declaration

```swift
enum ImageQuality
```

## Topics

### Quality Settings
- [XCTAttachment.ImageQuality.original](xctattachment/imagequality/original.md)
  Original image quality, represented as a lossless PNG image.
- [XCTAttachment.ImageQuality.medium](xctattachment/imagequality/medium.md)
  Medium image quality, represented as a high quality lossy JPEG image.
- [XCTAttachment.ImageQuality.low](xctattachment/imagequality/low.md)
  Low image quality, represented as a highly compressed lossy JPEG image.
### Initializers
- [init?(rawValue: Int)](xctattachment/imagequality/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [convenience init(image: UIImage)](xctattachment/init(image:).md)
  Creates an attachment containing a PNG representation of the provided image.
- [convenience init(image: UIImage, quality: XCTAttachment.ImageQuality)](xctattachment/init(image:quality:).md)
  Creates an attachment containing a representation of the provided image at the requested image quality.
- [convenience init(screenshot: XCUIScreenshot)](xctattachment/init(screenshot:).md)
  Creates an attachment containing a PNG representation of the provided screenshot.
- [convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)](xctattachment/init(screenshot:quality:).md)
  Creates an attachment containing a representation of the provided screenshot at the requested image quality.
- [class XCUIScreenshot](../xcuiautomation/xcuiscreenshot.md)
  A captured image of a screen, app, or UI element state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/imagequality)*