# barsSwipeTransition()

**Framework**: Core Image  
**Kind**: method

Transitions between two images by removing rectangular portions of an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func barsSwipeTransition() -> any CIFilter & CIBarsSwipeTransition
```

## Mentions

- [Customizing Image Transitions](customizing-image-transitions.md)

#### Return Value

The transition image.

#### Discussion

This method applies the bar swipe transition filter to an image. The effect transitions from one image to another by a series of moving bars passing over the target image.

The bar swipe transition filter uses the following properties:

The following code creates a filter that produces falling bars from the input image to transition to the target image:

```swift
func barSwipe(inputImage: CIImage, targetImage: CIImage) -> CIImage {
    let barSwipeTranstion = CIFilter.barsSwipeTransition()
    barSwipeTranstion.inputImage = inputImage
    barSwipeTranstion.targetImage = targetImage
    barSwipeTranstion.time = 0.5
    barSwipeTranstion.angle = 0.09
    barSwipeTranstion.width = 30
    barSwipeTranstion.barOffset = 10   
    return barSwipeTranstion.outputImage!
}
```

![Three photographs. In the photo on the left, multiple sets of small purple flowers are photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall city building with two trees directly in front of the building. The center photograph is a snapshot of the moment that the bar swipe transition creates, where the left photo slowly fades away by sized bars moving out of frame, revealing the city building.](https://docs-assets.developer.apple.com/published/c751699d5a8e3963e169c131ecb5edd4/media-3616431%402x.png)

## See Also

- [class func accordionFoldTransition() -> any CIFilter & CIAccordionFoldTransition](cifilter-swift.class/accordionfoldtransition.md)
  Transitions by folding and crossfading an image to reveal the target image.
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
- [class func swipeTransition() -> any CIFilter & CISwipeTransition](cifilter-swift.class/swipetransition.md)
  Gradually transitions from one image to another with a swiping motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/barsswipetransition())*