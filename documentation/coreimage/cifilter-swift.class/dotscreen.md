# dotScreen()

**Framework**: Core Image  
**Kind**: method

Creates a monochrome image with a series of dots to add detail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func dotScreen() -> any CIFilter & CIDotScreen
```

#### Return Value

The modified image.

#### Discussion

This method applies a dot screen filter to an image. The effect generates a monochrome image containing a series of dots creating detail. The halftone effect is a set of lines, dots, or circles that contain detail. When viewing the image from a distance, the markings blend together, creating the illusion of continuous lines and shapes. Print media commonly uses this effect.

The dot screen filter uses the following properties:

The following code creates a filter that produces an image containing monochrome dots of detail on a black background:

```swift
func dot (inputImage: CIImage) -> CIImage {
    let dotScreen = CIFilter.dotScreen()
    dotScreen.inputImage = inputImage
    dotScreen.angle = 0
    dotScreen.center = CGPoint(x: 2016, y: 1512)
    dotScreen.width = 35
    dotScreen.sharpness = 0.7
    return dotScreen.outputImage!
}
```

![Two photographs of a wooden barrel of green artichokes. The artichokes are crisp with good lighting. The photo on the left has no modifications to color or detail. In the photo on the right, a dot screen filter is applied, resulting in the image becoming monochrome with an overlay of small dots creating the detail of the image.](https://docs-assets.developer.apple.com/published/8dfb12e72fcd303b50be1aec2f9b8818/media-3595912%402x.png)

## See Also

- [class func circularScreen() -> any CIFilter & CICircularScreen](cifilter-swift.class/circularscreen.md)
  Adds a circular overlay to an image.
- [class func cmykHalftone() -> any CIFilter & CICMYKHalftone](cifilter-swift.class/cmykhalftone.md)
  Adds a series of colorful dots to an image.
- [class func hatchedScreen() -> any CIFilter & CIHatchedScreen](cifilter-swift.class/hatchedscreen.md)
  Creates a monochrome image with a series of lines to add detail.
- [class func lineScreen() -> any CIFilter & CILineScreen](cifilter-swift.class/linescreen.md)
  Creates a monochrome image with a series of small lines to add detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/dotscreen())*