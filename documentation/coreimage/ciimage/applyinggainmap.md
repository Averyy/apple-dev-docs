# applyingGainMap(_:)

**Framework**: Core Image  
**Kind**: method

Create an image that applies a gain map Core Image image to the received Core Image image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func applyingGainMap(_ gainmap: CIImage) -> CIImage
```

#### Return Value

 An autoreleased [`CIImage`](ciimage.md) instance or the received image.

#### Discussion

The gain map image can be obtained by creating a [`CIImage`](ciimage.md) instance from `NSURL`/`NSData` and setting the [`auxiliaryHDRGainMap`](ciimageoption/auxiliaryhdrgainmap.md) option set to `@YES`.

If the gain map [`CIImage`](ciimage.md) instance doesn’t have the needed [`properties`](ciimage/properties.md) metadata, the received image will be returned as-is.

## See Also

- [func applyingGainMap(CIImage, headroom: Float) -> CIImage](ciimage/applyinggainmap(_:headroom:).md)
  Create an image that applies a gain map Core Image image with a specified headroom to the received Core Image image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/applyinggainmap(_:))*