# modTransition()

**Framework**: Core Image  
**Kind**: method

Transitions between two images by applying irregularly shaped holes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func modTransition() -> any CIFilter & CIModTransition
```

#### Return Value

The transition image.

#### Discussion

This method applies the mod transition filter to an image. The effect transitions from the input image to the output image by revealing the target image through irregularly shaped holes.

The mod transition filter uses the following properties:

The following code creates a filter that transitions from the input image to the target image by creating a series of irregular shaped holes.

```swift
func mod(inputImage: CIImage, targetImage: CIImage) -> CIImage {
    let modTransition = CIFilter.modTransition()
    modTransition.inputImage = inputImage
    modTransition.targetImage = targetImage
    modTransition.center = CGPoint(x: 390, y: 392)
    modTransition.time = 0.5
    modTransition.angle = 0.09
    modTransition.radius = 150
    modTransition.compression = 523   
    return modTransition.outputImage!
}
```

![Three photographs. In the photo on the left, there are multiple small purple flowers photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall building with two trees directly in front of the building. In the center photograph, a mod transition filter is applied, resulting in a still photo of the moving transition. The left photograph is overlaid on the photo on the right while transitioning by a series of irregular circles that spread to reveal the city photograph.](https://docs-assets.developer.apple.com/published/498ace3776691dba2816238b2c43a202/media-3616428%402x.png)

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
- [class func pageCurlTransition() -> any CIFilter & CIPageCurlTransition](cifilter-swift.class/pagecurltransition.md)
  Simulates the curl of a page, revealing the target image.
- [class func pageCurlWithShadowTransition() -> any CIFilter & CIPageCurlWithShadowTransition](cifilter-swift.class/pagecurlwithshadowtransition.md)
  Simulates the curl of a page, revealing the target image with added shadow.
- [class func rippleTransition() -> any CIFilter & CIRippleTransition](cifilter-swift.class/rippletransition.md)
  Simulates a ripple in a pond to transiton from one image to another.
- [class func swipeTransition() -> any CIFilter & CISwipeTransition](cifilter-swift.class/swipetransition.md)
  Gradually transitions from one image to another with a swiping motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/modtransition())*