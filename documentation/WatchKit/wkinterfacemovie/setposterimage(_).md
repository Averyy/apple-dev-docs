# setPosterImage(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the poster image to display for the movie.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setPosterImage(_ posterImage: WKImage?)
```

```objc
- (void) setPosterImage:(WKImage *) posterImage;
```

## Discussion

This method changes the poster image that is displayed for the movie.

## Parameters

- `posterImage`: The image to be displayed. Specifying `nil` removes the existing image, causing the watch interface to display nothing in the space previously occupied by the image.

## See Also

### Setting the Movie Attributes
- [func setMovieURL(URL)](./setmovieurl%28_%29.md)
  Sets the URL of the movie to play.
- [func setVideoGravity(WKVideoGravity)](./setvideogravity%28_%29.md)
  Sets the resizing behavior for the movie content.
- [func setLoops(Bool)](./setloops%28_%29.md)
  Sets a Boolean value indicating whether the movie plays in a continuous loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemovie/setposterimage(_:))*