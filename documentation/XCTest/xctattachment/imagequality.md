# XCTAttachment.ImageQuality

**Framework**: XCTest  
**Kind**: enum  
**Role**: Enumeration

Compression quality options for image-based attachments.

## Declaration

```swift
enum ImageQuality
```

```c
enum XCTImageQuality : NSInteger;
```

## Topics

### Quality Settings
- [XCTAttachment.ImageQuality.original](./imagequality/original.md)
  Original image quality, represented as a lossless PNG image.
- [XCTAttachment.ImageQuality.medium](./imagequality/medium.md)
  Medium image quality, represented as a high quality lossy JPEG image.
- [XCTAttachment.ImageQuality.low](./imagequality/low.md)
  Low image quality, represented as a highly compressed lossy JPEG image.
### Initializers
- [init?(rawValue: Int)](./imagequality/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating Attachments from Images and Screenshots
- [convenience init(image: UIImage)](./init%28image%29.md)
  Creates an attachment containing a PNG representation of the provided image.
- [convenience init(image: UIImage, quality: XCTAttachment.ImageQuality)](./init%28image,quality%29.md)
  Creates an attachment containing a representation of the provided image at the requested image quality.
- [convenience init(screenshot: XCUIScreenshot)](./init%28screenshot%29.md)
  Creates an attachment containing a PNG representation of the provided screenshot.
- [convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)](./init%28screenshot,quality%29.md)
  Creates an attachment containing a representation of the provided screenshot at the requested image quality.
- [class XCUIScreenshot](../../XCUIAutomation/xcuiscreenshot.md)
  A captured image of a screen, app, or UI element state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment/imagequality)*