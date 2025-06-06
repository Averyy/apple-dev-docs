# startAnimating()

**Framework**: Watchkit  
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

- [func startAnimatingWithImages(in: NSRange, duration: TimeInterval, repeatCount: Int)](wkimageanimatable/startanimatingwithimages(in:duration:repeatcount:).md)
  Animates the specified images with the given duration and repeat information.
- [func stopAnimating()](wkimageanimatable/stopanimating.md)
  Stops any in-progress animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimageanimatable/startanimating())*