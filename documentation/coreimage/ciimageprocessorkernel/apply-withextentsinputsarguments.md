# apply(withExtents:inputs:arguments:)

**Framework**: Core Image  
**Kind**: method

Call this method on your multiple-output Core Image Processor Kernel subclass to create an `NSArray` of new [`CIImage`](ciimage.md)s given the specified `NSArray` of extents.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class func apply(withExtents extents: [CIVector], inputs: [CIImage]?, arguments: [String : Any]?) throws -> [CIImage]
```

#### Return Value

 An autoreleased [`CIImage`](ciimage.md)

#### Discussion

The inputs and arguments will be retained so that your subclass can be called when the image is drawn.

This method will return `nil` and an error if:

- calling [`outputFormat(at:arguments:)`](ciimageprocessorkernel/outputformat(at:arguments:).md) on your subclass returns an unsupported format.
- calling [`formatForInput(at:)`](ciimageprocessorkernel/formatforinput(at:).md) on your subclass returns an unsupported format.
- your subclass does not implement [`process(with:arguments:output:)`](ciimageprocessorkernel/process(with:arguments:output:).md)

## Parameters

- `extents`: The array of bounding rectangles  that the   can produce.   Each rectangle in the array is an object created using     This method will return   if a rectangle in the array is empty.
- `inputs`: An array of   objects to use as input.
- `arguments`: This dictionary contains any additional parameters that the processor needs to   produce its output. The argument objects can be of any type but in order for   CoreImage  to cache intermediates, they must be of the following immutable types:   ,  ,  ,  ,  ,  ,  ,   ,  ,  ,  , or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/apply(withextents:inputs:arguments:))*