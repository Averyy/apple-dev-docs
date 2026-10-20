# setAutoplays(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value indicating whether the movie automatically begins playing as soon as the scene is presented.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func setAutoplays(_ autoplays: Bool)
```

```objc
- (void) setAutoplays:(BOOL) autoplays;
```

## Parameters

- `autoplays`: A Boolean value indicating the movie’s autoplay behavior. Specify [`true`](../../Swift/true.md) to have the movie automatically play as soon as the scene is presented. If set to [`false`](../../Swift/false.md), the inline movie object displays the poster image instead. The movie does not begin playing until the user taps the poster, or until you programmatically call either the [`play()`](./play%28%29.md) or [`playFromBeginning()`](./playfrombeginning%28%29.md) method. Defaults to [`true`](../../Swift/true.md).

## See Also

### Setting Movie Properties
- [func setLoops(Bool)](./setloops%28_%29.md)
  Sets a Boolean value indicating whether the movie plays in a continuous loop.
- [func setMovieURL(URL)](./setmovieurl%28_%29.md)
  Sets the URL of the movie to play.
- [func setPosterImage(WKImage?)](./setposterimage%28_%29.md)
  Sets the poster image to display for the movie.
- [func setVideoGravity(WKVideoGravity)](./setvideogravity%28_%29.md)
  Sets the resizing behavior for the movie content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setautoplays(_:))*