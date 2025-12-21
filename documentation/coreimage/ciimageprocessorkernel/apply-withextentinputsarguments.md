# apply(withExtent:inputs:arguments:)

**Framework**: Core Image  
**Kind**: method

Call this method on your Core Image Processor Kernel subclass to create a new image of the specified extent.

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

 An autoreleased [`CIImage`](ciimage.md)

#### Discussion

The inputs and arguments will be retained so that your subclass can be called when the image is drawn.

This method will return `nil` and an error if:

- calling [`outputFormat`](ciimageprocessorkernel/outputformat.md) on your subclass returns an unsupported format.
- calling [`formatForInput(at:)`](ciimageprocessorkernel/formatforinput(at:).md) on your subclass returns an unsupported format.
- your subclass does not implement [`process(with:arguments:output:)`](ciimageprocessorkernel/process(with:arguments:output:).md)

## Parameters

- `extent`: The bounding   of pixels that the   can produce.   This method will return   if extent is empty.
- `inputs`: An array of   objects to use as input.
- `arguments`: This dictionary contains any additional parameters that the processor needs to   produce its output. The argument objects can be of any type but in order for   CoreImage  to cache intermediates, they must be of the following immutable types:   ,  ,  ,  ,  ,  ,  ,   ,  ,  ,  , or  .

## See Also

- [class func formatForInput(at: Int32) -> CIFormat](ciimageprocessorkernel/formatforinput(at:).md)
  Override this class method if you want your any of the inputs to be in a specific pixel format.
- [class func process(with: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws](ciimageprocessorkernel/process(with:arguments:output:).md)
  Override this class method to implement your Core Image Processor Kernel subclass.
- [class func roi(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect](ciimageprocessorkernel/roi(forinput:arguments:outputrect:).md)
  Override this class method to implement your processor’s ROI callback.
- [class func roiTileArray(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]](ciimageprocessorkernel/roitilearray(forinput:arguments:outputrect:).md)
  Override this class method to implement your processor’s tiled ROI callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/apply(withextent:inputs:arguments:))*