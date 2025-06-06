# startAnimatingWithImages(in:duration:repeatCount:)

**Framework**: Watchkit  
**Kind**: method  
**Required**: Yes

Animates the specified images with the given duration and repeat information.

**Availability**:
- watchOS ?+

## Declaration

```swift
func startAnimatingWithImages(in imageRange: NSRange, duration: TimeInterval, repeatCount: Int)
```

#### Discussion

This method animates a subset of the images associated with the current image interface object. This method starts the animation from the first image in the specified range.

## Parameters

- `imageRange`: The range of images to be animated. The value   indicates the first image in the sequence, the value   the second image, and so on.
- `duration`: The time (in seconds) over which to animate a single loop of the images. Positive values cause the animation to start at the first frame in the sequence and end on the last frame. Negative values causes the animation to play in reverse order and end on the first frame in the sequence.
- `repeatCount`: The number of times to repeat the animation loop. Specify   to animate the images indefinitely.

## See Also

- [func startAnimating()](wkimageanimatable/startanimating.md)
  Begins animating the current sequence of images.
- [func stopAnimating()](wkimageanimatable/stopanimating.md)
  Stops any in-progress animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkimageanimatable/startanimatingwithimages(in:duration:repeatcount:))*