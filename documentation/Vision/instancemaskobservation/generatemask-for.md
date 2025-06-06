# generateMask(for:)

**Framework**: Vision  
**Kind**: method

Creates a low-resolution mask from the instances you specify.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func generateMask(for instances: IndexSet) throws -> CVPixelBuffer
```

#### Return Value

The pixel buffer that contains the mask.

## Parameters

- `instances`: An indexed set of selected instances, where   is the background.

## See Also

- [func generateMaskedImage(for: IndexSet, imageFrom: ImageRequestHandler, croppedToInstancesExtent: Bool) throws -> CVPixelBuffer](instancemaskobservation/generatemaskedimage(for:imagefrom:croppedtoinstancesextent:).md)
  Creates a high-resolution image with everything except for the instances you specify masked out.
- [func generateScaledMask(for: IndexSet, scaledToImageFrom: ImageRequestHandler) throws -> CVPixelBuffer](instancemaskobservation/generatescaledmask(for:scaledtoimagefrom:).md)
  Creates a high-resolution mask representing a combination of the instances you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/instancemaskobservation/generatemask(for:))*