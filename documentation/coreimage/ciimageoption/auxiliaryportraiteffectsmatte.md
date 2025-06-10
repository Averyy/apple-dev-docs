# auxiliaryPortraitEffectsMatte

**Framework**: Core Image  
**Kind**: property

The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static let auxiliaryPortraitEffectsMatte: CIImageOption
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) containing a Boolean [`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [static let applyOrientationProperty: CIImageOption](ciimageoption/applyorientationproperty.md)
  The key for transforming an image according to orientation metadata.
- [static let auxiliaryDepth: CIImageOption](ciimageoption/auxiliarydepth.md)
  The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [static let auxiliaryDisparity: CIImageOption](ciimageoption/auxiliarydisparity.md)
  The key into the properties dictionary indicating whether to return an auxiliary disparity image.
- [static let auxiliaryHDRGainMap: CIImageOption](ciimageoption/auxiliaryhdrgainmap.md)
- [static let auxiliarySemanticSegmentationGlassesMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationglassesmatte.md)
- [static let auxiliarySemanticSegmentationHairMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationhairmatte.md)
- [static let auxiliarySemanticSegmentationSkinMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationskinmatte.md)
- [static let auxiliarySemanticSegmentationSkyMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationskymatte.md)
- [static let auxiliarySemanticSegmentationTeethMatte: CIImageOption](ciimageoption/auxiliarysemanticsegmentationteethmatte.md)
- [static let cacheImmediately: CIImageOption](ciimageoption/cacheimmediately.md)
- [static let colorSpace: CIImageOption](ciimageoption/colorspace.md)
  The key for a color space.
- [static let expandToHDR: CIImageOption](ciimageoption/expandtohdr.md)
  A Boolean value that indicates whether to read Gain Map HDR images as HDR.
- [static let nearestSampling: CIImageOption](ciimageoption/nearestsampling.md)
  The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.
- [static let properties: CIImageOption](ciimageoption/properties.md)
  The key for image metadata properties.
- [static let providerTileSize: CIImageOption](ciimageoption/providertilesize.md)
  A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/auxiliaryportraiteffectsmatte)*