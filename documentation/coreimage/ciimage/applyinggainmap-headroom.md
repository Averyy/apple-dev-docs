# applyingGainMap(_:headroom:)

**Framework**: Core Image  
**Kind**: method

Create an image that applies a gain map Core Image image with a specified headroom to the received Core Image image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func applyingGainMap(_ gainmap: CIImage, headroom: Float) -> CIImage
```

#### Return Value

 An autoreleased [`CIImage`](ciimage.md) instance or the received image.

## Parameters

- `gainmap`: The gain map   instance to apply to the receiver.
- `headroom`: A float value that specify how much headroom the resulting image should have.   The headroom value will be limited to between 1.0 (i.e. SDR) and   the full headroom allowed by the gain map.

## See Also

- [func applyingGainMap(CIImage) -> CIImage](ciimage/applyinggainmap(_:).md)
  Create an image that applies a gain map Core Image image to the received Core Image image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/applyinggainmap(_:headroom:))*