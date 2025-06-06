# WKInterfaceMovie

**Framework**: Watchkit  
**Kind**: class

An interface element that lets you play video and audio content in your watchOS app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceMovie
```

#### Overview

A movie object displays a poster image with a play button on top of it. When the user taps the play button, WatchKit plays the movie in a modal interface.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a movie object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates any needed movie objects and assigns them to their associated outlets. At that point, you can use those objects to make changes to the onscreen content.

Do not attempt to play audio or video content while gathering heart rate data using Health Kit. If you use this class to play media, WatchKit automatically disables the gathering of heart rate data.

##### Supported Media Formats

The following table lists the encoding information to use when creating media files to play on a user’s Apple Watch. For audio and video assets played directly from your app, keep your clips relatively short. Short clips consume less space on disk, use less power, and take less time to download.

| Media type | Recommended encoding |
| --- | --- |
| Video assets | Video codec: H.264 High Profile ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Bit rate: 160 kpbs at up to 30 fps ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Full screen resolution: 208 x 260 in portrait orientation ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 16:9 resolution: 320 x 180 in landscape orientation ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Audio bit rate: 32 kpbs stereo |
| Audio-only assets | Bit rate: 32 kbps stereo |

##### Interface Builder Configuration Options

Xcode lets you configure information about your movie interface object in your storyboard file. The following table lists the attributes you can configure and their meaning.

| Attribute | Description |
| --- | --- |
| Video Gravity | The sizing behavior for the movie. Use this attribute to determine whether the movie maintains its aspect ratio and how it fills the available space. You can also configure this value programmatically using the [`setVideoGravity(_:)`](wkinterfacemovie/setvideogravity(_:).md) method. |
| Poster Image | The placeholder image to display for your movie. When the user taps the poser image, the movie interface object presents a modal sheet with the actual movie contents. You can also configure this value programmatically using the [`setPosterImage(_:)`](wkinterfacemovie/setposterimage(_:).md) method. |

## Topics

### Setting the Movie Attributes
- [func setMovieURL(URL)](wkinterfacemovie/setmovieurl(_:).md)
  Sets the URL of the movie to play.
- [func setVideoGravity(WKVideoGravity)](wkinterfacemovie/setvideogravity(_:).md)
  Sets the resizing behavior for the movie content.
- [func setPosterImage(WKImage?)](wkinterfacemovie/setposterimage(_:).md)
  Sets the poster image to display for the movie.
- [func setLoops(Bool)](wkinterfacemovie/setloops(_:).md)
  Sets a Boolean value indicating whether the movie plays in a continuous loop.
### Initializing for SwiftUI
- [init()](wkinterfacemovie/init.md)
  Creates a movie object for use in SwiftUI.

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
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md)
  An interface element that displays a video’s poster image and supports inline playing of the video.
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md)
  An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit.
- [enum WKVideoGravity](wkvideogravity.md)
  Constants indicating the appearance of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemovie)*