# disintegrateWithMaskTransition()

**Framework**: Core Image  
**Kind**: method

Transitions between two images using a mask image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func disintegrateWithMaskTransition() -> any CIFilter & CIDisintegrateWithMaskTransition
```

#### Return Value

The transition image.

#### Discussion

This method applies the disintegrate with mask transition filter to an image. The effect transitions from one image to another using the shapes defined by the mask image.

The disintegrate with mask transition filter uses the following properties:

The following code creates a filter that produces a transition between the input and target images starting in the area’s outline in the mask image:

```swift
func disintergrate(inputImage: CIImage, targetImage: CIImage, maskImage: CIImage) -> CIImage {
    let disintergrateTransition  = CIFilter.disintegrateWithMaskTransition()
    disintergrateTransition.inputImage = inputImage
    disintergrateTransition.targetImage = targetImage
    disintergrateTransition.maskImage = maskImage
    disintergrateTransition.time = 0.5
    disintergrateTransition.shadowRadius = 8
    disintergrateTransition.shadowDensity = 0.65
    disintergrateTransition.shadowOffset = CGPoint(x: 0, y: -1)
    return disintergrateTransition.outputImage!
}
```

![Three photographs. In the photo on the left, there are multiple small purple flowers photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall building with two trees directly in front of the building. In the center photo, a disintegrate with mask transition filter is applied, resulting in a still photograph of the moving transition. The left photograph is overlaid on the right photo while slowly transitioning to the city image, with a slow fade of the flower image to the city image with added brightness.](https://docs-assets.developer.apple.com/published/486c03fd6a217a1e60232f3d2b08e780/media-3616430%402x.png)

## See Also

- [class func accordionFoldTransition() -> any CIFilter & CIAccordionFoldTransition](cifilter-swift.class/accordionfoldtransition.md)
  Transitions by folding and crossfading an image to reveal the target image.
- [class func barsSwipeTransition() -> any CIFilter & CIBarsSwipeTransition](cifilter-swift.class/barsswipetransition.md)
  Transitions between two images by removing rectangular portions of an image.
- [class func copyMachineTransition() -> any CIFilter & CICopyMachineTransition](cifilter-swift.class/copymachinetransition.md)
  Simulates the effect of a copy machine scanner light to transiton between two images.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/disintegratewithmasktransition())*