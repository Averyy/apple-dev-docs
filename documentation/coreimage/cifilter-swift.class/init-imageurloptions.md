# init(imageURL:options:)

**Framework**: Core Image  
**Kind**: init

Creates a filter that allows the processing of RAW images.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init!(imageURL url: URL!, options: [CIRAWFilterOption : Any]! = [:])
```

#### Return Value

A [`CIFilter`](cifilter-swift.class.md) object.

#### Discussion

The first step when working with RAW images in Core Image is to process the image using either [`init(imageData:options:)`](cifilter-swift.class/init(imagedata:options:).md) or [`init(imageURL:options:)`](cifilter-swift.class/init(imageurl:options:).md). These initializers create a [`CIFilter`](cifilter-swift.class.md) object with an [`outputImage`](cifilter-swift.class/outputimage.md) which is a [`CIImage`](ciimage.md) representation of the supplied RAW image.

The newly created filter object allows you fine control over the image processing that isn’t available when working with processed images such a JPEG. The following listing shows how to create a Core Image filter based on a URL named `imageURL`. The image is processed so that its neutral temperature is set to 2,000 Kelvin (giving a blue tint) and its baseline exposure doubled. Finally, a Core Image vignette filter is applied to the processed image in the same way it would be with any other source image:

```objc
let rawFilter = CIFilter(imageURL: imageURL, options: nil)
rawFilter?.setValue(2000,    
                    forKey: kCIInputNeutralTemperatureKey)
if let baselineExposure = rawFilter?.value(forKey: kCIInputBaselineExposureKey) as? NSNumber {    
    rawFilter?.setValue(baselineExposure.doubleValue * 2.5,                        forKey: kCIInputBaselineExposureKey)
}
let vignettedImage = rawFilter?.outputImage?.applyingFilter(    
    "CIVignette",    
    withInputParameters: [kCIInputIntensityKey: 5])
if let outputImage = vignettedImage {    
    imageView.image = UIImage(ciImage: outputImage)
}
```

> ❗ **Important**:  Core Image doesn’t process the supplied RAW image until the filter’s [`outputImage`](cifilter-swift.class/outputimage.md) is rendered. For this reason, if you supply this initializer with a RAW image of an unsupported format, the filter object will be initialized but its [`outputImage`](cifilter-swift.class/outputimage.md) will be `nil`.

## Parameters

- `url`: The location of a RAW image file.
- `options`: An options dictionary.  You can pass any of the keys defined in  .

## See Also

- [init!(CVPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(cvpixelbuffer:properties:options:).md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(imagedata:options:).md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](cirawfilteroption.md)
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](cifilter-swift.class/serializedxmp(from:inputimageextent:).md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](cifilter-swift.class/filterarray(fromserializedxmp:inputimageextent:error:).md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](cifilter-swift.class/supportedrawcameramodels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(imageurl:options:))*