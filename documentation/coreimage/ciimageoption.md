# CIImageOption

**Framework**: Core Image  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct CIImageOption
```

## Topics

### Initializers
- [init(rawValue: String)](ciimageoption/init(rawvalue:).md)
### Type Properties
- [static let applyOrientationProperty: CIImageOption](ciimageoption/applyorientationproperty.md)
  The key for transforming an image according to orientation metadata.
- [static let auxiliaryDepth: CIImageOption](ciimageoption/auxiliarydepth.md)
  The key into the properties dictionary indicating whether to return an auxiliary depth image.
- [static let auxiliaryDisparity: CIImageOption](ciimageoption/auxiliarydisparity.md)
  The key into the properties dictionary indicating whether to return an auxiliary disparity image.
- [static let auxiliaryHDRGainMap: CIImageOption](ciimageoption/auxiliaryhdrgainmap.md)
- [static let auxiliaryPortraitEffectsMatte: CIImageOption](ciimageoption/auxiliaryportraiteffectsmatte.md)
  The key into the properties dictionary indicating whether to return auxiliary portrait effects matte.
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
- [static let providerUserInfo: CIImageOption](ciimageoption/provideruserinfo.md)
  A key for data needed by the image provider. The associated value is an object that contains the needed data.
- [static let textureFormat: CIImageOption](ciimageoption/textureformat.md)
  The key for an OpenGL texture format.
- [static let textureTarget: CIImageOption](ciimageoption/texturetarget.md)
  The key for an OpenGL texture target.
- [static let toneMapHDRtoSDR: CIImageOption](ciimageoption/tonemaphdrtosdr.md)
- [static let contentHeadroom: CIImageOption](ciimageoption/contentheadroom.md)
- [static let applyCleanAperture: CIImageOption](ciimageoption/applycleanaperture.md)
  A Boolean value to control whether an image created with a CVPixelBuffer or an IOSurface should be cropped and offset according clean aperture attachments.
- [static let contentAverageLightLevel: CIImageOption](ciimageoption/contentaveragelightlevel.md)
  A value for overriding the automatic behavior of the Content Average Light Level property when creating an image.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption)*