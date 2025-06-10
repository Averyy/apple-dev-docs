# init(cgImage:)

**Framework**: Core Image  
**Kind**: init

Initializes an image object with a Quartz 2D image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init(cgImage image: CGImage)
```

#### Return Value

The initialized image object.

## Parameters

- `image`: A Quartz 2D image ( ) object. For more information, see   and  .

## See Also

- [class func empty() -> CIImage](ciimage/empty.md)
  Creates and returns an empty image object.
- [init?(image: UIImage)](ciimage/init(image:).md)
  Initializes an image object with the specified UIKit image object.
- [init?(image: UIImage, options: [CIImageOption : Any]?)](ciimage/init(image:options:).md)
  Initializes an image object with the specified UIKit image object, using the specified options.
- [init?(contentsOf: URL)](ciimage/init(contentsof:).md)
  Initializes an image object by reading an image from a URL.
- [init?(contentsOf: URL, options: [CIImageOption : Any]?)](ciimage/init(contentsof:options:).md)
  Initializes an image object by reading an image from a URL, using the specified options.
- [init(cgImage: CGImage, options: [CIImageOption : Any]?)](ciimage/init(cgimage:options:).md)
  Initializes an image object with a Quartz 2D image, using the specified options.
- [init(cgImageSource: CGImageSource, index: Int, options: [CIImageOption : Any]?)](ciimage/init(cgimagesource:index:options:).md)
- [init?(data: Data)](ciimage/init(data:).md)
  Initializes an image object with the supplied image data.
- [init?(data: Data, options: [CIImageOption : Any]?)](ciimage/init(data:options:).md)
  Initializes an image object with the supplied image data, using the specified options.
- [init(bitmapData: Data, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace?)](ciimage/init(bitmapdata:bytesperrow:size:format:colorspace:).md)
  Initializes an image object with bitmap data.
- [init?(bitmapImageRep: NSBitmapImageRep)](ciimage/init(bitmapimagerep:).md)
  Initializes an image object with the specified bitmap image representation.
- [init(imageProvider: Any, size: Int, Int, format: CIFormat, colorSpace: CGColorSpace?, options: [CIImageOption : Any]?)](ciimage/init(imageprovider:size:_:format:colorspace:options:).md)
  Initializes an image object with  data provided by an image provider, using the specified options.
- [init?(depthData: AVDepthData)](ciimage/init(depthdata:).md)
- [init?(depthData: AVDepthData, options: [String : Any]?)](ciimage/init(depthdata:options:).md)
- [init?(portaitEffectsMatte: AVPortraitEffectsMatte)](ciimage/init(portaiteffectsmatte:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(cgimage:))*