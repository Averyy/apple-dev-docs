# apply(withExtent:inputs:arguments:)

**Framework**: Core Image  
**Kind**: method

Method to override when applying a custom image processor kernel to an image and returning the result.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func apply(withExtent extent: CGRect, inputs: [CIImage]?, arguments: [String : Any]?) throws -> CIImage
```

#### Return Value

The output image resulting from applying the custom image processor kernel.

#### Discussion

Applies a custom image processor kernel to an image.

> ❗ **Important**:  Core Image will concatenate filters in a network into as fewer kernels as possible, avoiding the creation of intermediate buffers. However, it is unable to do this with image processor kernels.

## Parameters

- `extent`: The extent of the image to which to apply the kernel.
- `inputs`: The source images to process.

## See Also

- [class func formatForInput(at: Int32) -> CIFormat](ciimageprocessorkernel/formatforinput(at:).md)
  Method to override for returning the image processing kernel’s input pixel format.
- [class func process(with: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws](ciimageprocessorkernel/process(with:arguments:output:).md)
  Method to override for customizing the kernel’s image processing.
- [class func roi(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect](ciimageprocessorkernel/roi(forinput:arguments:outputrect:).md)
  Method to override for determining specific region of input image required to process in rendering a specified region of the output image.
- [class func roiTileArray(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]](ciimageprocessorkernel/roitilearray(forinput:arguments:outputrect:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/apply(withextent:inputs:arguments:))*