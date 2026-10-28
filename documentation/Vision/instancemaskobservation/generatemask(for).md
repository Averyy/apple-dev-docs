# generateMask(for:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Creates a low-resolution mask from the instances you specify.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
func generateMask(for instances: IndexSet) throws -> CVPixelBuffer
```

## Return Value

The pixel buffer that contains the mask.

## Parameters

- `instances`: An indexed set of selected instances, where `0` is the background.

## See Also

### Generating a mask
- [func generateMaskedImage(for: IndexSet, imageFrom: ImageRequestHandler, croppedToInstancesExtent: Bool) throws -> CVPixelBuffer](./generatemaskedimage%28for,imagefrom,croppedtoinstancesextent%29.md)
  Creates a high-resolution image with everything except for the instances you specify masked out.
- [func generateScaledMask(for: IndexSet, scaledToImageFrom: ImageRequestHandler) throws -> CVPixelBuffer](./generatescaledmask%28for,scaledtoimagefrom%29.md)
  Creates a high-resolution mask representing a combination of the instances you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/instancemaskobservation/generatemask(for:))*