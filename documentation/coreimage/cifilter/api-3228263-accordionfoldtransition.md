# accordionFoldTransition()

**Framework**: Core Image  
**Kind**: clm

Transitions by folding and crossfading an image to reveal the target image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func accordionFoldTransition() -> any CIFilter & CIAccordionFoldTransition
```

#### Return_value

The transition image.

#### Discussion

This method applies the accordion fold transition filter to an image. The effect transitions from one image to another by unfolding and crossfading.

The accordion fold transition filter uses the following properties:

The following code creates a filter that produces folds in the input image and fades to the target image:

```swift
func accordionFold(inputImage: CIImage, targetImage: CIImage) -> CIImage {
    let accordionFoldTransiton = CIFilter.accordionFoldTransition()
    accordionFoldTransiton.inputImage = inputImage
    accordionFoldTransiton.targetImage = targetImage
    accordionFoldTransiton.time = 0.5
    accordionFoldTransiton.numberOfFolds = 6
    accordionFoldTransiton.foldShadowAmount = 2
    return accordionFoldTransiton.outputImage!
}
```

![Three photographs. In the photo on the left, multiple sets of small purple flowers are photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall city building with two trees directly in front of the building. In the center photo, a bar swipe transition is applied, resulting in a still photograph of the moving transition. The left photograph is overlaid on the right photo and slowly folding up to reveal the target image.](https://docs-assets.developer.apple.com/published/53586dafb8/rendered2x-1591037435.png)

## See Also

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
- [class func swipeTransition() -> any CIFilter & CISwipeTransition](cifilter/3228420-swipetransition.md)
  Gradually transitions from one image to another with a swiping motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228263-accordionfoldtransition)*