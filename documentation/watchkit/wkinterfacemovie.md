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

## Overview

A movie object displays a poster image with a play button on top of it. When the user taps the play button, WatchKit plays the movie in a modal interface.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a movie object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates any needed movie objects and assigns them to their associated outlets. At that point, you can use those objects to make changes to the onscreen content.

Do not attempt to play audio or video content while gathering heart rate data using Health Kit. If you use this class to play media, WatchKit automatically disables the gathering of heart rate data.

The following table lists the encoding information to use when creating media files to play on a user’s Apple Watch. For audio and video assets played directly from your app, keep your clips relatively short. Short clips consume less space on disk, use less power, and take less time to download.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Media type'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Recommended encoding'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Video assets', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Video codec: H.264 High Profile '}, {'identifier': 'spacer', 'type': 'image'}, {'type': 'text', 'text': ' Bit rate: 160 kpbs at up to 30 fps '}, {'identifier': 'spacer', 'type': 'image'}, {'type': 'text', 'text': ' Full screen resolution: 208 x 260 in portrait orientation '}, {'identifier': 'spacer', 'type': 'image'}, {'type': 'text', 'text': ' 16:9 resolution: 320 x 180 in landscape orientation '}, {'identifier': 'spacer', 'type': 'image'}, {'type': 'text', 'text': ' Audio bit rate: 32 kpbs stereo'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Audio-only assets', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Bit rate: 32 kbps stereo', 'type': 'text'}]}] |

Xcode lets you configure information about your movie interface object in your storyboard file. The following table lists the attributes you can configure and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'inlineContent': [{'type': 'text', 'text': 'Attribute'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Description'}], 'type': 'paragraph'}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Video Gravity'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The sizing behavior for the movie. Use this attribute to determine whether the movie maintains its aspect ratio and how it fills the available space. You can also configure this value programmatically using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceMovie/setVideoGravity(_:)'}, {'type': 'text', 'text': ' method.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Poster Image', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The placeholder image to display for your movie. When the user taps the poser image, the movie interface object presents a modal sheet with the actual movie contents. You can also configure this value programmatically using the '}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceMovie/setPosterImage(_:)'}, {'type': 'text', 'text': ' method.'}]}] |

## Topics

### Setting the Movie Attributes
- [func setMovieURL(URL)](setmovieurl(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie/setmovieurl(_:)))
  Sets the URL of the movie to play.
- [func setVideoGravity(WKVideoGravity)](setvideogravity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie/setvideogravity(_:)))
  Sets the resizing behavior for the movie content.
- [func setPosterImage(WKImage?)](setposterimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie/setposterimage(_:)))
  Sets the poster image to display for the movie.
- [func setLoops(Bool)](setloops(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie/setloops(_:)))
  Sets a Boolean value indicating whether the movie plays in a continuous loop.
### Initializing for SwiftUI
- [init()](init().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie/init()))
  Creates a movie object for use in SwiftUI.

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
- [class WKImage](wkimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage))
- [protocol WKImageAnimatable](wkimageanimatable.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimageanimatable))
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie))
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera))
- [enum WKVideoGravity](wkvideogravity.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemovie)*