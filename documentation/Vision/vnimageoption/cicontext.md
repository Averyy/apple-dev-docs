# ciContext

**Framework**: Vision  
**Kind**: property  
**Role**: Type Property

An option key to specify the context to use in the handler’s Core Image operations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let ciContext: VNImageOption
```

```c
extern VNImageOption const VNImageOptionCIContext;
```

## Discussion

If this key isn’t specified, Vision will create its own [`CIContext`](../../CoreImage/cicontext.md).

Specify a [`CIContext`](../../CoreImage/cicontext.md) when you’ve used one in processing an input [`CIImage`](../../CoreImage/ciimage.md) or executing a [`CIFilter`](../../CoreImage/cifilter-swift.class.md) chain, so you can save the cost of creating a new context.

## See Also

### Options Dictionary Keys
- [static let properties: VNImageOption](./properties.md)
  The dictionary from the image source that contains the metadata for algorithms like horizon detection.
- [static let cameraIntrinsics: VNImageOption](./cameraintrinsics.md)
  An option to specify the camera intrinstics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageoption/cicontext)*