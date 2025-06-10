# VNImageOption

**Framework**: Vision  
**Kind**: struct

An option key passed into an image request handler that takes an auxiliary image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct VNImageOption
```

#### Discussion

Pass an option key into the [`VNImageRequestHandler`](vnimagerequesthandler.md) instance on creation or request.  Option keys are used to describe specific properties of an image or specify how an image needs to be handled.

## Topics

### Initializers
- [init(rawValue: String)](vnimageoption/init(rawvalue:).md)
  Initializes an option key using its string name.
### Options Dictionary Keys
- [static let properties: VNImageOption](vnimageoption/properties.md)
  The dictionary from the image source that contains the metadata for algorithms like horizon detection.
- [static let cameraIntrinsics: VNImageOption](vnimageoption/cameraintrinsics.md)
  An option to specify the camera intrinstics.
- [static let ciContext: VNImageOption](vnimageoption/cicontext.md)
  An option key to specify the context to use in the handler’s Core Image operations.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageoption)*