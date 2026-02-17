# setMovieURL(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the URL of the movie to play.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setMovieURL(_ URL: URL)
```

#### Discussion

Movies must be local to the device before playback begins. If you specify a URL that is on a remote server, Apple Watch downloads the movie before playing it.

## Parameters

- `URL`: The URL must be in a shared location that can be accessed by both the Watch app interface and the WatchKit extension. For more information, see   in  .

## See Also

- [func setVideoGravity(WKVideoGravity)](wkinterfacemovie/setvideogravity(_:).md)
  Sets the resizing behavior for the movie content.
- [func setPosterImage(WKImage?)](wkinterfacemovie/setposterimage(_:).md)
  Sets the poster image to display for the movie.
- [func setLoops(Bool)](wkinterfacemovie/setloops(_:).md)
  Sets a Boolean value indicating whether the movie plays in a continuous loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemovie/setmovieurl(_:))*