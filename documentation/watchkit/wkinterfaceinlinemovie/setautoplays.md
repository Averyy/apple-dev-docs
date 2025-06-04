# setAutoplays(_:)

**Framework**: Watchkit  
**Kind**: method

Sets a Boolean value indicating whether the movie automatically begins playing as soon as the scene is presented.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func setAutoplays(_ autoplays: Bool)
```

## Parameters

- `autoplays`: A Boolean value indicating the movie’s autoplay behavior. Specify   to have the movie automatically play as soon as the scene is presented. If set to  , the inline movie object displays the poster image instead. The movie does not begin playing until the user taps the poster, or until you programmatically call either the   or   method. Defaults to  .

## See Also

- [func setLoops(Bool)](setloops(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setloops(_:)))
- [func setMovieURL(URL)](setmovieurl(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setmovieurl(_:)))
- [func setPosterImage(WKImage?)](setposterimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setposterimage(_:)))
- [func setVideoGravity(WKVideoGravity)](setvideogravity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setvideogravity(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setautoplays(_:))*