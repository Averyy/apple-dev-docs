# ciContext

**Framework**: Vision  
**Kind**: property

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

#### Discussion

If this key isn’t specified, Vision will create its own [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext).

Specify a [`CIContext`](https://developer.apple.com/documentation/coreimage/cicontext) when you’ve used one in processing an input [`CIImage`](https://developer.apple.com/documentation/coreimage/ciimage) or executing a [`CIFilter`](https://developer.apple.com/documentation/coreimage/cifilter) chain, so you can save the cost of creating a new context.

## See Also

- [static let properties: VNImageOption](vnimageoption/properties.md)
  The dictionary from the image source that contains the metadata for algorithms like horizon detection.
- [static let cameraIntrinsics: VNImageOption](vnimageoption/cameraintrinsics.md)
  An option to specify the camera intrinstics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageoption/cicontext)*