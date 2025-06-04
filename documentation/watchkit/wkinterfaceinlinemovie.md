# WKInterfaceInlineMovie

**Framework**: Watchkit  
**Kind**: class

An interface element that displays a video’s poster image and supports inline playing of the video.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKInterfaceInlineMovie
```

## Overview

In watchOS 2.0, you had to display video content using a [`WKInterfaceMovie`](https://developer.apple.com/documentation/watchkit/wkinterfacemovie) object. This object displayed a poster image for the video, and when the user tapped the poster image, the video was shown in a separate, full-screen, modal view.

The [`WKInterfaceInlineMovie`](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie) object also lets you display a poster image for your video; however, when the poster is tapped, this video replaces the poster image and plays in place. You can also create videos that play automatically as soon as the scene is presented.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a movie object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates any needed inline movie objects and assigns them to their associated outlets. At that point, you can use those objects to make changes to the onscreen content.

Do not attempt to play audio or video content while gathering heart rate data using Health Kit. If you use this class to play media, WatchKit automatically disables the gathering of heart rate data.

The following table lists the encoding information to use when creating media files to play on a user’s Apple Watch. For audio and video assets played directly from your app, keep your clips relatively short. Short clips consume less space on disk, use less power, and take less time to download.

| r | o | w |
| --- | --- | --- |
| [{'inlineContent': [{'type': 'text', 'text': 'Media type'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Recommended encoding'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Video assets'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Video codec: H.264 High Profile ', 'type': 'text'}, {'type': 'image', 'identifier': 'spacer'}, {'text': ' Bit rate: 160 kpbs at up to 30 fps ', 'type': 'text'}, {'type': 'image', 'identifier': 'spacer'}, {'text': ' Full screen resolution: 208 x 260 in portrait orientation ', 'type': 'text'}, {'type': 'image', 'identifier': 'spacer'}, {'text': ' 16:9 resolution: 320 x 180 in landscape orientation ', 'type': 'text'}, {'type': 'image', 'identifier': 'spacer'}, {'text': ' Audio bit rate: 32 kpbs stereo', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Audio-only assets', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Bit rate: 32 kbps stereo'}], 'type': 'paragraph'}] |

Xcode lets you configure information about your inline movie interface object in your storyboard file. The following table lists the attributes you can configure and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Attribute', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Description', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Video Gravity', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The sizing behavior for the movie. Use this attribute to determine whether the movie maintains its aspect ratio and how it fills the available space. You can also configure this value programmatically using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceInlineMovie/setVideoGravity(_:)'}, {'type': 'text', 'text': ' method.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Poster Image', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The placeholder image to display for your movie. When the user taps the poster image, the movie begins to play inline. You can also configure this value programmatically using the '}, {'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceInlineMovie/setPosterImage(_:)', 'isActive': True, 'type': 'reference'}, {'type': 'text', 'text': ' method.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Loop'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'A boolean value indicating whether the movie plays in a continuous loop. If checked, the movie plays in a continuous loop. If unchecked, the movie plays once and then stops. You can also configure this value programmatically using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceInlineMovie/setLoops(_:)'}, {'type': 'text', 'text': ' method.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Autoplay', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'A boolean value indicating whether the movie automatically plays as soon as the interface is presented. If checked, the movie automatically begins playing. If unchecked, the inline movie object displays the poster image instead. The movie does not begin playing until the user taps the poster, or until you programmatically call either the '}, {'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceInlineMovie/play()', 'type': 'reference', 'isActive': True}, {'type': 'text', 'text': ' or '}, {'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceInlineMovie/playFromBeginning()', 'type': 'reference', 'isActive': True}, {'type': 'text', 'text': ' method. You can also configure this value programmatically using the '}, {'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceInlineMovie/setAutoplays(_:)', 'type': 'reference', 'isActive': True}, {'type': 'text', 'text': ' method.'}]}] |

## Topics

### Setting Movie Properties
- [func setAutoplays(Bool)](setautoplays(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setautoplays(_:)))
  Sets a Boolean value indicating whether the movie automatically begins playing as soon as the scene is presented.
- [func setLoops(Bool)](setloops(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setloops(_:)))
  Sets a Boolean value indicating whether the movie plays in a continuous loop.
- [func setMovieURL(URL)](setmovieurl(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setmovieurl(_:)))
  Sets the URL of the movie to play.
- [func setPosterImage(WKImage?)](setposterimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setposterimage(_:)))
  Sets the poster image to display for the movie.
- [func setVideoGravity(WKVideoGravity)](setvideogravity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setvideogravity(_:)))
  Sets the resizing behavior for the movie content.
### Controlling Playback
- [func pause()](pause().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/pause()))
  Pauses the movie.
- [func play()](play().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/play()))
  Plays the movie.
- [func playFromBeginning()](playfrombeginning().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/playfrombeginning()))
  Plays the movie from the beginning.
### Initializing for SwiftUI
- [init()](init().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/init()))
  Creates an inline movie object for use in SwiftUI.

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
- [class WKInterfaceMovie](wkinterfacemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie))
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera))
- [enum WKVideoGravity](wkvideogravity.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie)*