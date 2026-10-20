# setLoops(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value indicating whether the movie plays in a continuous loop.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setLoops(_ loops: Bool)
```

```objc
- (void) setLoops:(BOOL) loops;
```

## Parameters

- `loops`: A Boolean value indicating the looping behavior. Specify [`true`](../../Swift/true.md) to play the movie in a continuous loop or [`false`](../../Swift/false.md) to play the movie once and then stop playback.

## See Also

### Setting the Movie Attributes
- [func setMovieURL(URL)](./setmovieurl%28_%29.md)
  Sets the URL of the movie to play.
- [func setVideoGravity(WKVideoGravity)](./setvideogravity%28_%29.md)
  Sets the resizing behavior for the movie content.
- [func setPosterImage(WKImage?)](./setposterimage%28_%29.md)
  Sets the poster image to display for the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemovie/setloops(_:))*