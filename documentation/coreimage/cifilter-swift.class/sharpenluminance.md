# sharpenLuminance()

**Framework**: Core Image  
**Kind**: method

Applies a sharpening effect to an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func sharpenLuminance() -> any CIFilter & CISharpenLuminance
```

#### Return Value

The modified image.

#### Discussion

This method applies the sharpen luminance filter to an image. The effect increases image detail by adjusting the luminance of each pixel within the `radius` property. Sharpening the luminance doesn’t effect the chroma data of each pixel.

The bicubic sharpen luminance filter uses the following properties:

The following code creates a filter that results in detail from the sign in the image to be more visible:

```swift
func sharpen (inputImage: CIImage) -> CIImage? {
    let sharpenLuminance = CIFilter.sharpenLuminance()
    sharpenLuminance.inputImage = inputImage
    sharpenLuminance.radius = 10
    sharpenLuminance.sharpness = 1
    return sharpenLuminance.outputImage!
}
```

![Two photographs of a downtown sidewalk with trees, a blue square highlighting the end of the sidewalk with a bike lane and street sign displayed. The photo on the left has no modifications to color. In the photo on the right a sharpen luminance filter has been applied resulting in the black of the bike lane sign becoming darker.](https://docs-assets.developer.apple.com/published/9fa76bd8c6a3167408db44c5fddadffb/media-3595821%402x.png)

## See Also

- [class func unsharpMask() -> any CIFilter & CIUnsharpMask](cifilter-swift.class/unsharpmask.md)
  Increases an image’s contrast between two colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/sharpenluminance())*