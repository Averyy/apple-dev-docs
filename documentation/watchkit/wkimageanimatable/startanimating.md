# startAnimating()

**Framework**: WatchKit  
**Kind**: method  
**Required**: Yes

Begins animating the current sequence of images.

**Availability**:
- watchOS ?+

## Declaration

```swift
func startAnimating()
```

#### Discussion

If the image data contains multiple images, calling this method begins animating through those images, starting at the first image. The animation uses the duration value specified in your storyboard file.

If the current image contains only a single image, this method does nothing.

## See Also

- [func startAnimatingWithImages(in: NSRange, duration: TimeInterval, repeatCount: Int)](startanimatingwithimages(in:duration:repeatcount:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimageanimatable/startanimatingwithimages(in:duration:repeatcount:)))
  Animates the specified images with the given duration and repeat information.
- [func stopAnimating()](stopanimating().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimageanimatable/stopanimating()))
  Stops any in-progress animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimageanimatable/startanimating())*