# hatchedScreen()

**Framework**: Core Image  
**Kind**: method

Creates a monochrome image with a series of lines to add detail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func hatchedScreen() -> any CIFilter & CIHatchedScreen
```

#### Return Value

The modified image.

#### Discussion

This method applies a hatched screen filter to an image. The effect generates a monochrome image containing a series of lines in hatched pattern to create detail. The halftone effect is a set of lines, dots, or circles that contain detail. When viewing the image from a distance, the markings blend together, creating the illusion of continuous lines and shapes. The effect is often used in print media for more efficient printing.

The hatched screen filter uses the following properties:

The following code creates a filter that produces a monochrome image containing lines of detail on a black background:

```swift
func hatched(inputImage: CIImage) -> CIImage {
    let hatchedScreen = CIFilter.hatchedScreen()
    hatchedScreen.inputImage = inputImage
    hatchedScreen.center = CGPoint(x: 2016, y: 1512)
    hatchedScreen.angle = 10
    hatchedScreen.width = 35
    hatchedScreen.sharpness = 0.7
    return hatchedScreen.outputImage!
}
```

![Two photographs of wooden barrel of green artichokes. The artichokes are crisp with good lighting. The photo on the left has no modifications to color or detail. In the photo on the right, a hatched screen filter is applied, resulting in a lighter, grayscale image with an overlay of small lines in a hatched pattern, creating the detail of the image.](https://docs-assets.developer.apple.com/published/d95bfbb2d1541d005276bd8e53ad7990/media-3595917%402x.png)

## See Also

- [class func circularScreen() -> any CIFilter & CICircularScreen](cifilter-swift.class/circularscreen.md)
  Adds a circular overlay to an image.
- [class func cmykHalftone() -> any CIFilter & CICMYKHalftone](cifilter-swift.class/cmykhalftone.md)
  Adds a series of colorful dots to an image.
- [class func dotScreen() -> any CIFilter & CIDotScreen](cifilter-swift.class/dotscreen.md)
  Creates a monochrome image with a series of dots to add detail.
- [class func lineScreen() -> any CIFilter & CILineScreen](cifilter-swift.class/linescreen.md)
  Creates a monochrome image with a series of small lines to add detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/hatchedscreen())*