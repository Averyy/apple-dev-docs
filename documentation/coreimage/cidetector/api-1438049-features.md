# features(in:)

**Framework**: Core Image  
**Kind**: instm

Searches for features in an image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func features(in image: CIImage) -> [CIFeature]
```

#### Return_value

An array of [`CIFeature`](cifeature.md) objects. Each object represents a feature detected in the image.

## Parameters

- `image`: The image you want to examine.

## See Also

- [func features(in: CIImage, options: [String : Any]?) -> [CIFeature]](cidetector/1438189-features.md)
  Searches for features in an image based on the specified image orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetector/1438049-features)*