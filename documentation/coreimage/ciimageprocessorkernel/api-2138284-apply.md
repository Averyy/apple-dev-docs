# apply(withExtent:inputs:arguments:)

**Framework**: Core Image  
**Kind**: clm

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
class func apply(withExtent extent: CGRect, inputs: [CIImage]?, arguments args: [String : Any]?) throws -> CIImage
```

#### Return_value

The output image resulting from applying the custom image processor kernel.

#### Discussion

Applies a custom image processor kernel to an image. 

> ❗ **Important**: Core Image will concatenate filters in a network into as fewer kernels as possible, avoiding the creation of intermediate buffers. However, it is unable to do this with image processor kernels. 

Core Image will concatenate filters in a network into as fewer kernels as possible, avoiding the creation of intermediate buffers. However, it is unable to do this with image processor kernels. 

## Parameters

- `extent`: The extent of the image to which to apply the kernel.
- `input`: The input source image to process.
- `args`: Dictionary of arguments mapping keys such as   to their values.
- `error`: Pointer to the   object into which processing errors will be written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2138284-apply)*