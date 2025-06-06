# features(in:options:)

**Framework**: Core Image  
**Kind**: instm

Searches for features in an image based on the specified image orientation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func features(in image: CIImage, options: [String : Any]? = nil) -> [CIFeature]
```

#### Return_value

An array of [`CIFeature`](cifeature.md) objects. Each object represents a feature detected in the image.

## Parameters

- `image`: The image you want to examine.
- `options`: A dictionary that specifies feature detection options. See   for allowed keys and their possible values.

## See Also

- [func features(in: CIImage) -> [CIFeature]](cidetector/1438049-features.md)
  Searches for features in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetector/1438189-features)*