# WKImageAnimatable

**Framework**: Watchkit  
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
- [func startAnimating()](wkimageanimatable/startanimating.md)
  Begins animating the current sequence of images.
- [func startAnimatingWithImages(in: NSRange, duration: TimeInterval, repeatCount: Int)](wkimageanimatable/startanimatingwithimages(in:duration:repeatcount:).md)
  Animates the specified images with the given duration and repeat information.
- [func stopAnimating()](wkimageanimatable/stopanimating.md)
  Stops any in-progress animations.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [WKInterfaceGroup](wkinterfacegroup.md)
- [WKInterfaceImage](wkinterfaceimage.md)

## See Also

- [class WKInterfaceImage](wkinterfaceimage.md)
  An image that can be displayed in the interface of your watchOS app.
- [class WKImage](wkimage.md)
  A wrapper for images you use with a picker interface.
- [class WKInterfaceMovie](wkinterfacemovie.md)
  An interface element that lets you play video and audio content in your watchOS app.
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md)
  An interface element that displays a video’s poster image and supports inline playing of the video.
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md)
  An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit.
- [enum WKVideoGravity](wkvideogravity.md)
  Constants indicating the appearance of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimageanimatable)*