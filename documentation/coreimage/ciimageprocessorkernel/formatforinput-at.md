# formatForInput(at:)

**Framework**: Core Image  
**Kind**: method

Method to override for returning the image processing kernel’s input pixel format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func formatForInput(at inputIndex: Int32) -> CIFormat
```

#### Return Value

Core Image pixel format [`CIFormat`](ciformat.md) constant revealing the processor’s input pixel format.

#### Discussion

Override this method and the [`outputFormat`](ciimageprocessorkernel/outputformat.md) property getter to customize your processor’s input and output pixel format.

The format must be one of [`CIFormat`](ciformat.md): [`BGRA8`](ciformat/bgra8.md), [`RGBAh`](ciformat/rgbah.md), [`RGBAf`](ciformat/rgbaf.md), or [`R8`](ciformat/r8.md).  If the [`outputFormat`](ciimageprocessorkernel/outputformat.md) is 0, then the output will be a supported format that best matches the rendering context’s [`workingFormat`](cicontext/workingformat.md).

## See Also

- [class func apply(withExtent: CGRect, inputs: [CIImage]?, arguments: [String : Any]?) throws -> CIImage](ciimageprocessorkernel/apply(withextent:inputs:arguments:).md)
  Method to override when applying a custom image processor kernel to an image and returning the result.
- [class func process(with: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws](ciimageprocessorkernel/process(with:arguments:output:).md)
  Method to override for customizing the kernel’s image processing.
- [class func roi(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect](ciimageprocessorkernel/roi(forinput:arguments:outputrect:).md)
  Method to override for determining specific region of input image required to process in rendering a specified region of the output image.
- [class func roiTileArray(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]](ciimageprocessorkernel/roitilearray(forinput:arguments:outputrect:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/formatforinput(at:))*