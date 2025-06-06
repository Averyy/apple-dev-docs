# WKInterfaceHMCamera

**Framework**: Watchkit  
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

The camera interface object in your Watch app must be connected to a [`WKInterfaceHMCamera`](wkinterfacehmcamera.md) outlet in your WatchKit extension for the camera to be visible in your watchOS app’s user interface.

## Topics

### Setting the Camera Source
- [func setCameraSource(HMCameraSource?)](wkinterfacehmcamera/setcamerasource(_:).md)
  Set the HomeKit camera source displayed by this interface object.
### Initializing for SwiftUI
- [init()](wkinterfacehmcamera/init.md)
  Creates a camera for use in SwiftUI.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [enum WKVideoGravity](wkvideogravity.md)
  Constants indicating the appearance of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera)*