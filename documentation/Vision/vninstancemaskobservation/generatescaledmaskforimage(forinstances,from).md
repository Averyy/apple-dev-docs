# generateScaledMaskForImage(forInstances:from:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Creates a high-resolution mask where everything becomes transparent black, except for the instances you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func generateScaledMaskForImage(forInstances instances: IndexSet, from requestHandler: VNImageRequestHandler) throws -> CVPixelBuffer
```

```objc
- (CVPixelBufferRef) generateScaledMaskForImageForInstances:(NSIndexSet *) instances fromRequestHandler:(VNImageRequestHandler *) requestHandler error:(NSError **) error;
```

## Return Value

The pixel buffer that contains the image.

## Parameters

- `instances`: The collection of instances.
- `requestHandler`: The image request callback.

## See Also

### Creating a Mask
- [func generateMask(forInstances: IndexSet) throws -> CVPixelBuffer](./generatemask%28forinstances%29.md)
  Creates a low-resolution mask from the instances you specify.
- [func generateMaskedImage(ofInstances: IndexSet, from: VNImageRequestHandler, croppedToInstancesExtent: Bool) throws -> CVPixelBuffer](./generatemaskedimage%28ofinstances,from,croppedtoinstancesextent%29.md)
  Creates a high-resolution image where everything becomes transparent black, except for the instances you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vninstancemaskobservation/generatescaledmaskforimage(forinstances:from:))*