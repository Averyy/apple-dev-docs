# VNImageOption

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An option key passed into an image request handler that takes an auxiliary image.

## Declaration

```swift
struct VNImageOption
```

```c
typedef NSString * VNImageOption;
```

#### Discussion

Pass an option key into the [`VNImageRequestHandler`](./vnimagerequesthandler.md) instance on creation or request.  Option keys are used to describe specific properties of an image or specify how an image needs to be handled.

## Topics

### Initializers
- [init(rawValue: String)](./vnimageoption/init%28rawvalue%29.md)
  Initializes an option key using its string name.
### Options Dictionary Keys
- [static let properties: VNImageOption](./vnimageoption/properties.md)
  The dictionary from the image source that contains the metadata for algorithms like horizon detection.
- [static let cameraIntrinsics: VNImageOption](./vnimageoption/cameraintrinsics.md)
  An option to specify the camera intrinstics.
- [static let ciContext: VNImageOption](./vnimageoption/cicontext.md)
  An option key to specify the context to use in the handler’s Core Image operations.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnimageoption)*