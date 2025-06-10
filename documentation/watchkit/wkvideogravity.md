# WKVideoGravity

**Framework**: WatchKit  
**Kind**: enum

Constants indicating the appearance of video content.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
enum WKVideoGravity
```

## Topics

### Constants
- [WKVideoGravity.resizeAspect](wkvideogravity/resizeaspect.md)
  Content is resized to fit the bounds rectangle, preserving the original aspect ratio of the content. Content that does not completely fill the bounds rectangle is centered in the partial axis.
- [WKVideoGravity.resizeAspectFill](wkvideogravity/resizeaspectfill.md)
  Content is resized to fill the bounds rectangle completely while preserving the original aspect ratio of the content. This option results in cropping of the edges of the video in the axis it exceeds.
- [WKVideoGravity.resize](wkvideogravity/resize.md)
  Content is resized to fit the entire bounds rectangle. This option does not preserve the original aspect ratio of the content.
### Initializers
- [init?(rawValue: Int)](wkvideogravity/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class WKInterfaceImage](wkinterfaceimage.md)
  An image that can be displayed in the interface of your watchOS app.
- [class WKImage](wkimage.md)
  A wrapper for images you use with a picker interface.
- [protocol WKImageAnimatable](wkimageanimatable.md)
  A collection of methods you can use to control the playback of animated images.
- [class WKInterfaceMovie](wkinterfacemovie.md)
  An interface element that lets you play video and audio content in your watchOS app.
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md)
  An interface element that displays a video’s poster image and supports inline playing of the video.
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md)
  An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkvideogravity)*