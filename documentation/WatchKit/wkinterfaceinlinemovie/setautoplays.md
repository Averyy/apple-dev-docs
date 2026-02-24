# setAutoplays(_:)

**Framework**: WatchKit  
**Kind**: method

Sets a Boolean value indicating whether the movie automatically begins playing as soon as the scene is presented.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func setAutoplays(_ autoplays: Bool)
```

## Parameters

- `autoplays`: A Boolean value indicating the movie’s autoplay behavior. Specify [`true`](https://developer.apple.com/documentation/Swift/true) to have the movie automatically play as soon as the scene is presented. If set to [`false`](https://developer.apple.com/documentation/Swift/false), the inline movie object displays the poster image instead. The movie does not begin playing until the user taps the poster, or until you programmatically call either the [`play()`](wkinterfaceinlinemovie/play().md) or [`playFromBeginning()`](wkinterfaceinlinemovie/playfrombeginning().md) method. Defaults to [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [func setLoops(Bool)](wkinterfaceinlinemovie/setloops(_:).md)
  Sets a Boolean value indicating whether the movie plays in a continuous loop.
- [func setMovieURL(URL)](wkinterfaceinlinemovie/setmovieurl(_:).md)
  Sets the URL of the movie to play.
- [func setPosterImage(WKImage?)](wkinterfaceinlinemovie/setposterimage(_:).md)
  Sets the poster image to display for the movie.
- [func setVideoGravity(WKVideoGravity)](wkinterfaceinlinemovie/setvideogravity(_:).md)
  Sets the resizing behavior for the movie content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setautoplays(_:))*