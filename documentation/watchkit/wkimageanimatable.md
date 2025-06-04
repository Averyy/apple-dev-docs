# WKImageAnimatable

**Framework**: WatchKit  
**Kind**: protocol

A collection of methods you can use to control the playback of animated images.

**Availability**:
- watchOS ?+

## Declaration

```swift
protocol WKImageAnimatable : NSObjectProtocol
```

#### Overview

Existing classes adopt this protocol and you use the methods to control the animation of those images. Do not adopt this protocol in your own classes.

## Topics

### Animating an Image Sequence
- [func startAnimating()](startanimating().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimageanimatable/startanimating()))
  Begins animating the current sequence of images.
- [func startAnimatingWithImages(in: NSRange, duration: TimeInterval, repeatCount: Int)](startanimatingwithimages(in:duration:repeatcount:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimageanimatable/startanimatingwithimages(in:duration:repeatcount:)))
  Animates the specified images with the given duration and repeat information.
- [func stopAnimating()](stopanimating().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimageanimatable/stopanimating()))
  Stops any in-progress animations.

## Relationships

### Inherits From
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))
### Conforming Types
- [WKInterfaceGroup](wkinterfacegroup.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup))
- [WKInterfaceImage](wkinterfaceimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage))

## See Also

- [class WKInterfaceImage](wkinterfaceimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage))
  An image that can be displayed in the interface of your watchOS app.
- [class WKImage](wkimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage))
  A wrapper for images you use with a picker interface.
- [class WKInterfaceMovie](wkinterfacemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie))
  An interface element that lets you play video and audio content in your watchOS app.
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie))
  An interface element that displays a video’s poster image and supports inline playing of the video.
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera))
  An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit.
- [enum WKVideoGravity](wkvideogravity.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity))
  Constants indicating the appearance of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimageanimatable)*