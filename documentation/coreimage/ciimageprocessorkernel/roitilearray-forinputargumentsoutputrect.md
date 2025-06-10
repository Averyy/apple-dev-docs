# roiTileArray(forInput:arguments:outputRect:)

**Framework**: Core Image  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func roiTileArray(forInput inputIndex: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]
```

## See Also

- [class func apply(withExtent: CGRect, inputs: [CIImage]?, arguments: [String : Any]?) throws -> CIImage](ciimageprocessorkernel/apply(withextent:inputs:arguments:).md)
  Method to override when applying a custom image processor kernel to an image and returning the result.
- [class func formatForInput(at: Int32) -> CIFormat](ciimageprocessorkernel/formatforinput(at:).md)
  Method to override for returning the image processing kernel’s input pixel format.
- [class func process(with: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws](ciimageprocessorkernel/process(with:arguments:output:).md)
  Method to override for customizing the kernel’s image processing.
- [class func roi(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect](ciimageprocessorkernel/roi(forinput:arguments:outputrect:).md)
  Method to override for determining specific region of input image required to process in rendering a specified region of the output image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/roitilearray(forinput:arguments:outputrect:))*