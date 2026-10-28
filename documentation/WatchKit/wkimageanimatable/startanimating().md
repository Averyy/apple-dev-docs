# startAnimating()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Begins animating the current sequence of images.

**Availability**:
- watchOS

## Declaration

```swift
func startAnimating()
```

```objc
- (void) startAnimating;
```

## Discussion

If the image data contains multiple images, calling this method begins animating through those images, starting at the first image. The animation uses the duration value specified in your storyboard file.

If the current image contains only a single image, this method does nothing.

## See Also

### Animating an Image Sequence
- [func startAnimatingWithImages(in: NSRange, duration: TimeInterval, repeatCount: Int)](./startanimatingwithimages%28in,duration,repeatcount%29.md)
  Animates the specified images with the given duration and repeat information.
- [func stopAnimating()](./stopanimating%28%29.md)
  Stops any in-progress animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimageanimatable/startanimating())*