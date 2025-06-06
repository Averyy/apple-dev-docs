# swipeTransition()

**Framework**: Core Image  
**Kind**: clm

Gradually transitions from one image to another with a swiping motion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func swipeTransition() -> any CIFilter & CISwipeTransition
```

#### Return_value

The transition image.

#### Discussion

This method applies the swipe transition filter to an image. The effect transitions from the input image to the target image by simulating a swiping motion.

The swipe transition filter uses the following properties:

The following code creates a filter that transitions from the input image to the target image with a gradual fade from left to right.

```swift
func swipe(inputImage: CIImage, targetImage: CIImage) -> CIImage {
    let swipeTransiton = CIFilter.swipeTransition()
    swipeTransiton.inputImage = inputImage
    swipeTransiton.targetImage = targetImage
    swipeTransiton.extent = CGRect(x: 0, y: 0, width: 300, height: 300)
    swipeTransiton.time = 0.5
    swipeTransiton.angle = -0.7
    swipeTransiton.width = 203
    swipeTransiton.opacity = 0
    return swipeTransiton.outputImage!
}
```

![Three photographs. In the photo on the left, there are multiple small purple flowers photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall building with two trees directly in front of the building. In the center photograph, a swipe transition filter is applied, resulting in a still photo of the moving transition. The left photograph is overlaid on the photo on the right with a slow fade from the left of the flower photo, revealing the city building photograph under it.](https://docs-assets.developer.apple.com/published/7c8520ab36/rendered2x-1591037440.png)

## See Also

- [class func accordionFoldTransition() -> any CIFilter & CIAccordionFoldTransition](cifilter/3228263-accordionfoldtransition.md)
  Transitions by folding and crossfading an image to reveal the target image.
- [class func barsSwipeTransition() -> any CIFilter & CIBarsSwipeTransition](cifilter/3228270-barsswipetransition.md)
  Transitions between two images by removing rectangular portions of an image.
- [class func copyMachineTransition() -> any CIFilter & CICopyMachineTransition](cifilter/3228304-copymachinetransition.md)
  Simulates the effect of a copy machine scanner light to transiton between two images.
- [class func disintegrateWithMaskTransition() -> any CIFilter & CIDisintegrateWithMaskTransition](cifilter/3228312-disintegratewithmasktransition.md)
  Transitions between two images using a mask image.
- [class func dissolveTransition() -> any CIFilter & CIDissolveTransition](cifilter/3228314-dissolvetransition.md)
  Transitions between two images with a fade effect.
- [class func flashTransition() -> any CIFilter & CIFlashTransition](cifilter/3228326-flashtransition.md)
  Creates a flash of light to transition between two images.
- [class func modTransition() -> any CIFilter & CIModTransition](cifilter/3228363-modtransition.md)
  Transitions between two images by applying irregularly shaped holes.
- [class func pageCurlTransition() -> any CIFilter & CIPageCurlTransition](cifilter/3228375-pagecurltransition.md)
  Simulates the curl of a page, revealing the target image.
- [class func pageCurlWithShadowTransition() -> any CIFilter & CIPageCurlWithShadowTransition](cifilter/3228376-pagecurlwithshadowtransition.md)
  Simulates the curl of a page, revealing the target image with added shadow.
- [class func rippleTransition() -> any CIFilter & CIRippleTransition](cifilter/3228397-rippletransition.md)
  Simulates a ripple in a pond to transiton from one image to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228420-swipetransition)*