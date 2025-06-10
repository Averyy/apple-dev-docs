# roi(forInput:arguments:outputRect:)

**Framework**: Core Image  
**Kind**: method

Method to override for determining specific region of input image required to process in rendering a specified region of the output image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func roi(forInput inputIndex: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect
```

#### Return Value

Rectangle defining the region of the input image over which the kernel should execute.

#### Discussion

Override this method if your image processor needs to work with a larger or smaller region of interest in the input image than each corresponding region of the output image (for example, a blur filter, which samples several input pixels for each output pixel).

This will be called one or more times per render to determine the portion of the input images needed to render a given `outputRect` of the output.  This will not be called if there are 0 input images.

The default implementation simply returns `outputRect`.

## Parameters

- `arguments`: Dictionary of arguments mapping keys such as   to their values.
- `outputRect`: Rectangle defining the area of output that must be rendered.

## See Also

- [class func apply(withExtent: CGRect, inputs: [CIImage]?, arguments: [String : Any]?) throws -> CIImage](ciimageprocessorkernel/apply(withextent:inputs:arguments:).md)
  Method to override when applying a custom image processor kernel to an image and returning the result.
- [class func formatForInput(at: Int32) -> CIFormat](ciimageprocessorkernel/formatforinput(at:).md)
  Method to override for returning the image processing kernel’s input pixel format.
- [class func process(with: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws](ciimageprocessorkernel/process(with:arguments:output:).md)
  Method to override for customizing the kernel’s image processing.
- [class func roiTileArray(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]](ciimageprocessorkernel/roitilearray(forinput:arguments:outputrect:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/roi(forinput:arguments:outputrect:))*