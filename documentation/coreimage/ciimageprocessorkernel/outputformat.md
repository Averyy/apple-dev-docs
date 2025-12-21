# outputFormat

**Framework**: Core Image  
**Kind**: property

Override this class property if you want your processor’s output to be in a specific pixel format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class var outputFormat: CIFormat { get }
```

#### Discussion

The format must be one of `kCIFormatBGRA8`, `kCIFormatRGBAh`, `kCIFormatRGBAf` or `kCIFormatR8`. On iOS 12 and macOS 10.14, the formats `kCIFormatRh` and `kCIFormatRf` are also supported.

If the outputFormat is `0`, then the output will be a supported format that best matches the rendering context’s `/CIContext/workingFormat`.

If a processor returns data in a color space other than the context working color space, then call `/CIImage/imageByColorMatchingColorSpaceToWorkingSpace:` on the processor output. If a processor returns data as alpha-unpremultiplied RGBA data, then call, `/CIImage/imageByPremultiplyingAlpha` on the processor output.

## See Also

- [class var outputIsOpaque: Bool](ciimageprocessorkernel/outputisopaque.md)
  Override this class property if your processor’s output stores 1.0 into the alpha channel of all pixels within the output extent.
- [class var synchronizeInputs: Bool](ciimageprocessorkernel/synchronizeinputs.md)
  Override this class property to return false if you want your processor to be given input objects that have not been synchronized for CPU access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/outputformat)*