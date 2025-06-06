# setLoops(_:)

**Framework**: Watchkit  
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

- [func setAutoplays(Bool)](wkinterfaceinlinemovie/setautoplays(_:).md)
  Sets a Boolean value indicating whether the movie automatically begins playing as soon as the scene is presented.
- [func setMovieURL(URL)](wkinterfaceinlinemovie/setmovieurl(_:).md)
  Sets the URL of the movie to play.
- [func setPosterImage(WKImage?)](wkinterfaceinlinemovie/setposterimage(_:).md)
  Sets the poster image to display for the movie.
- [func setVideoGravity(WKVideoGravity)](wkinterfaceinlinemovie/setvideogravity(_:).md)
  Sets the resizing behavior for the movie content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setloops(_:))*