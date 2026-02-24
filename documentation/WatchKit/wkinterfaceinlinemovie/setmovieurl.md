# setMovieURL(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the URL of the movie to play.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func setMovieURL(_ URL: URL)
```

#### Discussion

Movies must be local to the device before playback begins. If you specify a URL that is on a remote server, Apple Watch downloads the movie before playing it.

## Parameters

- `URL`: The URL of the movie to play. The URL must be a file-based URL that refers to a movie or audio file in the appropriate format. The URL must be in a shared location that can be accessed by both the Watch app interface and the WatchKit extension. For more information, see [`Sharing Data`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/SharingData.html#//apple_ref/doc/uid/TP40014969-CH29) in [`App Programming Guide for watchOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969).

## See Also

- [func setAutoplays(Bool)](wkinterfaceinlinemovie/setautoplays(_:).md)
  Sets a Boolean value indicating whether the movie automatically begins playing as soon as the scene is presented.
- [func setLoops(Bool)](wkinterfaceinlinemovie/setloops(_:).md)
  Sets a Boolean value indicating whether the movie plays in a continuous loop.
- [func setPosterImage(WKImage?)](wkinterfaceinlinemovie/setposterimage(_:).md)
  Sets the poster image to display for the movie.
- [func setVideoGravity(WKVideoGravity)](wkinterfaceinlinemovie/setvideogravity(_:).md)
  Sets the resizing behavior for the movie content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setmovieurl(_:))*