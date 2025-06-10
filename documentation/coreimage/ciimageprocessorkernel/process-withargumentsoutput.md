# process(with:arguments:output:)

**Framework**: Core Image  
**Kind**: method

Method to override for customizing the kernel’s image processing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func process(with inputs: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws
```

#### Discussion

Override this method to perform custom image processing.

## Parameters

- `inputs`: Inputs to this processor stage.
- `arguments`: Dictionary of arguments mapping keys such as   to their values.
- `output`: The output image following processing.

## See Also

- [class func apply(withExtent: CGRect, inputs: [CIImage]?, arguments: [String : Any]?) throws -> CIImage](ciimageprocessorkernel/apply(withextent:inputs:arguments:).md)
  Method to override when applying a custom image processor kernel to an image and returning the result.
- [class func formatForInput(at: Int32) -> CIFormat](ciimageprocessorkernel/formatforinput(at:).md)
  Method to override for returning the image processing kernel’s input pixel format.
- [class func roi(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect](ciimageprocessorkernel/roi(forinput:arguments:outputrect:).md)
  Method to override for determining specific region of input image required to process in rendering a specified region of the output image.
- [class func roiTileArray(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]](ciimageprocessorkernel/roitilearray(forinput:arguments:outputrect:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/process(with:arguments:output:))*