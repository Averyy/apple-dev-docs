# process(with:arguments:outputs:)

**Framework**: Core Image  
**Kind**: method

Override this class method of your Core Image Processor Kernel subclass if it needs to produce multiple outputs.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class func process(with inputs: [any CIImageProcessorInput]?, arguments: [String : Any]?, outputs: [any CIImageProcessorOutput]) throws
```

#### Discussion

This supports 0, 1, 2 or more input images and 2 or more output images.

The class method will be called to produce the requested region of the output images given the required regions of the input images and other arguments.

> ❗ **Important**: This is a class method you cannot use or capture any state by accident. All the parameters that affect the output results must be passed to [`apply(withExtent:inputs:arguments:)`](ciimageprocessorkernel/apply(withextent:inputs:arguments:).md).

## Parameters

- `inputs`: An array of   that the class consumes to produce its output.   The   may be larger than the rect returned by  .
- `arguments`: The arguments dictionary that was passed to  .
- `outputs`: An array   that the   must provide results to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/process(with:arguments:outputs:))*