# WKImage

**Framework**: WatchKit  
**Kind**: class

A wrapper for images you use with a picker interface.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKImage
```

#### Overview

To create instances of this class, use one of the defined creation methods. Choose the method that best suits the image data you have. After creating the object, you can use associate it with a [`WKPickerItem`](wkpickeritem.md) object and use it in your picker interface.

## Topics

### Creating Image Objects
- [convenience init(image: UIImage)](wkimage/init(image:).md)
  Creates and returns an image object using the specified UIKit image.
- [convenience init(imageData: Data)](wkimage/init(imagedata:).md)
  Creates an image with the specified raw image data.
- [convenience init(imageName: String)](wkimage/init(imagename:).md)
  Creates an image by loading an image file from the Watch app bundle.
### Getting the Image Data
- [var image: UIImage?](wkimage/image.md)
  The UIKit image object
- [var imageData: Data?](wkimage/imagedata.md)
  The data object containing the raw image data.
- [var imageName: String?](wkimage/imagename.md)
  The name of the image to load from the Watch app’s bundle.

## Relationships

### Inherits From
- [NSObject](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
### Conforms To
- [CVarArg](https://developer.apple.com/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [NSCoding](https://developer.apple.com/documentation/Foundation/NSCoding)
- [NSCopying](https://developer.apple.com/documentation/Foundation/NSCopying)
- [NSObjectProtocol](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)
- [NSSecureCoding](https://developer.apple.com/documentation/Foundation/NSSecureCoding)

## See Also

- [class WKInterfaceImage](wkinterfaceimage.md)
  An image that can be displayed in the interface of your watchOS app.
- [protocol WKImageAnimatable](wkimageanimatable.md)
  A collection of methods you can use to control the playback of animated images.
- [class WKInterfaceMovie](wkinterfacemovie.md)
  An interface element that lets you play video and audio content in your watchOS app.
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md)
  An interface element that displays a video’s poster image and supports inline playing of the video.
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md)
  An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit.
- [enum WKVideoGravity](wkvideogravity.md)
  Constants indicating the appearance of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage)*