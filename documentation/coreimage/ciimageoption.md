# CIImageOption

**Framework**: Core Image  
**Kind**: struct

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct CIImageOption
```

## Topics

### Initializers
- [init(rawValue: String)](ciimageoption/2998473-init.md)
### Type Properties
- [static let applyOrientationProperty: CIImageOption](ciimageoption/2915369-applyorientationproperty.md)
  The key for transforming an image according to orientation metadata.
- [static let auxiliaryDepth: CIImageOption](ciimageoption/2890795-auxiliarydepth.md)
  The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [static let auxiliaryDisparity: CIImageOption](ciimageoption/2890794-auxiliarydisparity.md)
  The key into the properties dictionary indicating whether to return an auxiliary disparity image.
- [static let auxiliaryHDRGainMap: CIImageOption](ciimageoption/4172813-auxiliaryhdrgainmap.md)
- [static let auxiliaryPortraitEffectsMatte: CIImageOption](ciimageoption/2976441-auxiliaryportraiteffectsmatte.md)
  The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.
- [static let auxiliarySemanticSegmentationGlassesMatte: CIImageOption](ciimageoption/3547135-auxiliarysemanticsegmentationgla.md)
- [static let auxiliarySemanticSegmentationHairMatte: CIImageOption](ciimageoption/3152400-auxiliarysemanticsegmentationhai.md)
- [static let auxiliarySemanticSegmentationSkinMatte: CIImageOption](ciimageoption/3152401-auxiliarysemanticsegmentationski.md)
- [static let auxiliarySemanticSegmentationSkyMatte: CIImageOption](ciimageoption/3547136-auxiliarysemanticsegmentationsky.md)
- [static let auxiliarySemanticSegmentationTeethMatte: CIImageOption](ciimageoption/3152402-auxiliarysemanticsegmentationtee.md)
- [static let cacheImmediately: CIImageOption](ciimageoption/4226856-cacheimmediately.md)
- [static let colorSpace: CIImageOption](ciimageoption/1438131-colorspace.md)
  The key for a color space.
- [static let expandToHDR: CIImageOption](ciimageoption/4210206-expandtohdr.md)
  A Boolean value that indicates whether to read Gain Map HDR images as HDR.
- [static let nearestSampling: CIImageOption](ciimageoption/2867426-nearestsampling.md)
  The key into the properties dictionary to indicate whether to use nearest-neighbor sampling.
- [static let properties: CIImageOption](ciimageoption/1437679-properties.md)
  The key for image metadata properties.
- [static let providerTileSize: CIImageOption](ciimageoption/1437829-providertilesize.md)
  A key for the image tiles size. The associated value is an `NSArray` that contains`NSNumber` objects for the dimensions of the image tiles requested from the image provider.
- [static let providerUserInfo: CIImageOption](ciimageoption/1437989-provideruserinfo.md)
  A key for data needed by the image provider. The associated value is an object that contains the needed data.
- [static let textureFormat: CIImageOption](ciimageoption/1437934-textureformat.md)
  The key for an OpenGL texture format.
- [static let textureTarget: CIImageOption](ciimageoption/1437613-texturetarget.md)
  The key for an OpenGL texture target.
- [static let toneMapHDRtoSDR: CIImageOption](ciimageoption/3686984-tonemaphdrtosdr.md)
- [static let contentHeadroom: CIImageOption](ciimageoption/4438509-contentheadroom.md)

## Relationships

### Conforms To
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption)*