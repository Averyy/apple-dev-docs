# WKInterfaceHMCamera

**Framework**: WatchKit  
**Kind**: class

An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKInterfaceHMCamera
```

#### Overview

Do not subclass or create instances of this class yourself. Instead, define an outlet in your interface controller class and connect it to the corresponding object in your storyboard file. For example, to refer to a camera interface object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates the camera interface object and assigns it to its associated outlet. At that point, you can use the camera interface object to change to the onscreen content.

The camera interface object in your Watch app must be connected to a [`WKInterfaceHMCamera`](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera) outlet in your WatchKit extension for the camera to be visible in your watchOS app’s user interface.

## Topics

### Setting the Camera Source
- [func setCameraSource(HMCameraSource?)](setcamerasource(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera/setcamerasource(_:)))
  Set the HomeKit camera source displayed by this interface object.
### Initializing for SwiftUI
- [init()](init().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera/init()))
  Creates a camera for use in SwiftUI.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

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
- [enum WKVideoGravity](wkvideogravity.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity))
  Constants indicating the appearance of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera)*