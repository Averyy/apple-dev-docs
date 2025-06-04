# setLoops(_:)

**Framework**: WatchKit  
**Kind**: method

Sets a Boolean value indicating whether the movie plays in a continuous loop.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func setLoops(_ loops: Bool)
```

## Parameters

- `loops`: A Boolean value indicating the looping behavior. Specify   to play the movie in a continuous loop or   to play the movie once and then stop playback. Defaults to  .

## See Also

- [func setAutoplays(Bool)](setautoplays(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setautoplays(_:)))
  Sets a Boolean value indicating whether the movie automatically begins playing as soon as the scene is presented.
- [func setMovieURL(URL)](setmovieurl(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setmovieurl(_:)))
  Sets the URL of the movie to play.
- [func setPosterImage(WKImage?)](setposterimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setposterimage(_:)))
  Sets the poster image to display for the movie.
- [func setVideoGravity(WKVideoGravity)](setvideogravity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setvideogravity(_:)))
  Sets the resizing behavior for the movie content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setloops(_:))*