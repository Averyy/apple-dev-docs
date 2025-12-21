# swipeTransition()

**Framework**: Core Image  
**Kind**: method

Gradually transitions from one image to another with a swiping motion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func swipeTransition() -> any CIFilter & CISwipeTransition
```

#### Return Value

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

![Three photographs. In the photo on the left, there are multiple small purple flowers photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall building with two trees directly in front of the building. In the center photograph, a swipe transition filter is applied, resulting in a still photo of the moving transition. The left photograph is overlaid on the photo on the right with a slow fade from the left of the flower photo, revealing the city building photograph under it.](https://docs-assets.developer.apple.com/published/8e1514955c4016952827294deb940344/media-3616424%402x.png)

## See Also

- [class func accordionFoldTransition() -> any CIFilter & CIAccordionFoldTransition](cifilter-swift.class/accordionfoldtransition.md)
  Transitions by folding and crossfading an image to reveal the target image.
- [class func barsSwipeTransition() -> any CIFilter & CIBarsSwipeTransition](cifilter-swift.class/barsswipetransition.md)
  Transitions between two images by removing rectangular portions of an image.
- [class func copyMachineTransition() -> any CIFilter & CICopyMachineTransition](cifilter-swift.class/copymachinetransition.md)
  Simulates the effect of a copy machine scanner light to transiton between two images.
- [class func disintegrateWithMaskTransition() -> any CIFilter & CIDisintegrateWithMaskTransition](cifilter-swift.class/disintegratewithmasktransition.md)
  Transitions between two images using a mask image.
- [class func dissolveTransition() -> any CIFilter & CIDissolveTransition](cifilter-swift.class/dissolvetransition.md)
  Transitions between two images with a fade effect.
- [class func flashTransition() -> any CIFilter & CIFlashTransition](cifilter-swift.class/flashtransition.md)
  Creates a flash of light to transition between two images.
- [class func modTransition() -> any CIFilter & CIModTransition](cifilter-swift.class/modtransition.md)
  Transitions between two images by applying irregularly shaped holes.
- [class func pageCurlTransition() -> any CIFilter & CIPageCurlTransition](cifilter-swift.class/pagecurltransition.md)
  Simulates the curl of a page, revealing the target image.
- [class func pageCurlWithShadowTransition() -> any CIFilter & CIPageCurlWithShadowTransition](cifilter-swift.class/pagecurlwithshadowtransition.md)
  Simulates the curl of a page, revealing the target image with added shadow.
- [class func rippleTransition() -> any CIFilter & CIRippleTransition](cifilter-swift.class/rippletransition.md)
  Simulates a ripple in a pond to transiton from one image to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/swipetransition())*