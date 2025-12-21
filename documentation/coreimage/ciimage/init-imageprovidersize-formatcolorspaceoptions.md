# init(imageProvider:size:_:format:colorSpace:options:)

**Framework**: Core Image  
**Kind**: init

Initializes an image object based on pixels from an image provider object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(imageProvider provider: Any, size width: Int, _ height: Int, format: CIFormat, colorSpace: CGColorSpace?, options: [CIImageOption : Any]? = nil)
```

#### Return Value

 An initialized [`CIImage`](ciimage.md) object based on the data provider.

#### Discussion

Core Image retains the provider object until the image is deallocated. The image provider object will not be called until the image is rendered.

## Parameters

- `provider`: An object that implements the   protocol.
- `width`: The width of the image.
- `height`: The height of the image.
- `format`: The   of the provided pixels.
- `colorSpace`: The color space that the image is defined in.   If  , then the pixels will not be is not color matched to the Core Image working color space.
- `options`: A dictionary that contains various   keys that affect the resulting  . 
 The option   controls if and how the provider object is called in tiles.   The option   allows additional state to be passed to the provider object.

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
- [init(cgImage: CGImage)](ciimage/init(cgimage:).md)
  Initializes an image object with a Quartz 2D image.
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
- [init?(depthData: AVDepthData)](ciimage/init(depthdata:).md)
- [init?(depthData: AVDepthData, options: [String : Any]?)](ciimage/init(depthdata:options:).md)
- [init?(portaitEffectsMatte: AVPortraitEffectsMatte)](ciimage/init(portaiteffectsmatte:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/init(imageprovider:size:_:format:colorspace:options:))*