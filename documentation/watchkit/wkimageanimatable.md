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

## Overview

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
- [class WKImage](wkimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage))
- [class WKInterfaceMovie](wkinterfacemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie))
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie))
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera))
- [enum WKVideoGravity](wkvideogravity.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimageanimatable)*