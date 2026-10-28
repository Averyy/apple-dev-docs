# init(for:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a model container to use with a Core ML request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(for model: MLModel) throws
```

```objc
+ (instancetype) modelForMLModel:(MLModel *) model error:(NSError **) error;
```

## Discussion

This method may fail if the framework doesn’t support the Core ML model. For example, a model that doesn’t accept an image as any of its inputs will yield an [`VNErrorCode.invalidModel`](../vnerrorcode/invalidmodel.md) error.

## Parameters

- `model`: The model to create the model container from.

## See Also

### Initializing a Model
- [convenience init(forMLModel: MLModel) throws](./init%28formlmodel%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncoremlmodel/init(for:))*