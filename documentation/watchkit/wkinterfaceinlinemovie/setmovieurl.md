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

- `URL`: The URL must be in a shared location that can be accessed by both the Watch app interface and the WatchKit extension. For more information, see   in  .

## See Also

- [func setAutoplays(Bool)](setautoplays(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setautoplays(_:)))
  Sets a Boolean value indicating whether the movie automatically begins playing as soon as the scene is presented.
- [func setLoops(Bool)](setloops(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setloops(_:)))
  Sets a Boolean value indicating whether the movie plays in a continuous loop.
- [func setPosterImage(WKImage?)](setposterimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setposterimage(_:)))
  Sets the poster image to display for the movie.
- [func setVideoGravity(WKVideoGravity)](setvideogravity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setvideogravity(_:)))
  Sets the resizing behavior for the movie content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setmovieurl(_:))*