# stopAnimating()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Stops any in-progress animations.

**Availability**:
- watchOS

## Declaration

```swift
func stopAnimating()
```

```objc
- (void) stopAnimating;
```

## Discussion

If no animation is in progress, this method does nothing.

## See Also

### Animating an Image Sequence
- [func startAnimating()](./startanimating%28%29.md)
  Begins animating the current sequence of images.
- [func startAnimatingWithImages(in: NSRange, duration: TimeInterval, repeatCount: Int)](./startanimatingwithimages%28in,duration,repeatcount%29.md)
  Animates the specified images with the given duration and repeat information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimageanimatable/stopanimating())*