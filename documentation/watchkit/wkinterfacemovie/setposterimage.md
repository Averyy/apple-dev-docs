# setPosterImage(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the poster image to display for the movie.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setPosterImage(_ posterImage: WKImage?)
```

#### Discussion

This method changes the poster image that is displayed for the movie.

## Parameters

- `posterImage`: The image to be displayed. Specifying   removes the existing image, causing the watch interface to display nothing in the space previously occupied by the image.

## See Also

- [func setMovieURL(URL)](wkinterfacemovie/setmovieurl(_:).md)
  Sets the URL of the movie to play.
- [func setVideoGravity(WKVideoGravity)](wkinterfacemovie/setvideogravity(_:).md)
  Sets the resizing behavior for the movie content.
- [func setLoops(Bool)](wkinterfacemovie/setloops(_:).md)
  Sets a Boolean value indicating whether the movie plays in a continuous loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemovie/setposterimage(_:))*