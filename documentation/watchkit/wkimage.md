# WKImage

**Framework**: Watchkit  
**Kind**: class

A wrapper for images you use with a picker interface.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKImage
```

## Overview

To create instances of this class, use one of the defined creation methods. Choose the method that best suits the image data you have. After creating the object, you can use associate it with a [`WKPickerItem`](https://developer.apple.com/documentation/watchkit/wkpickeritem) object and use it in your picker interface.

## Topics

### Creating Image Objects
- [convenience init(image: UIImage)](init(image:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(image:)))
  Creates and returns an image object using the specified UIKit image.
- [convenience init(imageData: Data)](init(imagedata:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(imagedata:)))
  Creates an image with the specified raw image data.
- [convenience init(imageName: String)](init(imagename:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/init(imagename:)))
  Creates an image by loading an image file from the Watch app bundle.
### Getting the Image Data
- [var image: UIImage?](image.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/image))
  The UIKit image object
- [var imageData: Data?](imagedata.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/imagedata))
  The data object containing the raw image data.
- [var imageName: String?](imagename.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage/imagename))
  The name of the image to load from the Watch app’s bundle.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSCoding ([Apple Docs](https://developer.apple.com/documentation/Foundation/NSCoding))
- NSCopying ([Apple Docs](https://developer.apple.com/documentation/Foundation/NSCopying))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))
- NSSecureCoding ([Apple Docs](https://developer.apple.com/documentation/Foundation/NSSecureCoding))

## See Also

- [class WKInterfaceImage](wkinterfaceimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage))
- [protocol WKImageAnimatable](wkimageanimatable.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimageanimatable))
- [class WKInterfaceMovie](wkinterfacemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie))
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie))
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera))
- [enum WKVideoGravity](wkvideogravity.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimage)*