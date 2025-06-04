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
- [WKVideoGravity.resizeAspect](resizeaspect.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity/resizeaspect))
  Content is resized to fit the bounds rectangle, preserving the original aspect ratio of the content. Content that does not completely fill the bounds rectangle is centered in the partial axis.
- [WKVideoGravity.resizeAspectFill](resizeaspectfill.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity/resizeaspectfill))
  Content is resized to fill the bounds rectangle completely while preserving the original aspect ratio of the content. This option results in cropping of the edges of the video in the axis it exceeds.
- [WKVideoGravity.resize](resize.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity/resize))
  Content is resized to fit the entire bounds rectangle. This option does not preserve the original aspect ratio of the content.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [class WKInterfaceImage](wkinterfaceimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage))
  An image that can be displayed in the interface of your watchOS app.
- [class WKImage](wkimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage))
  A wrapper for images you use with a picker interface.
- [protocol WKImageAnimatable](wkimageanimatable.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimageanimatable))
  A collection of methods you can use to control the playback of animated images.
- [class WKInterfaceMovie](wkinterfacemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie))
  An interface element that lets you play video and audio content in your watchOS app.
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie))
  An interface element that displays a video’s poster image and supports inline playing of the video.
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera))
  An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkvideogravity)*