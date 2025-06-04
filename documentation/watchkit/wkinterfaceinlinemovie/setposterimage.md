# setPosterImage(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the poster image to display for the movie.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func setPosterImage(_ posterImage: WKImage?)
```

#### Discussion

This method changes the poster image that is displayed for the movie.

## Parameters

- `posterImage`: The image to be displayed. Specifying   removes the existing image, causing the watch interface to display nothing in the space previously occupied by the image.

## See Also

- [func setAutoplays(Bool)](setautoplays(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setautoplays(_:)))
  Sets a Boolean value indicating whether the movie automatically begins playing as soon as the scene is presented.
- [func setLoops(Bool)](setloops(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setloops(_:)))
  Sets a Boolean value indicating whether the movie plays in a continuous loop.
- [func setMovieURL(URL)](setmovieurl(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setmovieurl(_:)))
  Sets the URL of the movie to play.
- [func setVideoGravity(WKVideoGravity)](setvideogravity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setvideogravity(_:)))
  Sets the resizing behavior for the movie content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/setposterimage(_:))*