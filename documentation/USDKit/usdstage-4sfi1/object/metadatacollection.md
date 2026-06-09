# USDStage.Object.MetadataCollection

**Framework**: USDKit  
**Kind**: protocol

A scene graph object that possesses metadata.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol MetadataCollection
```

#### Overview

Prims, attributes, and relationships may have associated metadata. Metadata on an object is accessed by its name, which is a [`USDToken`](usdtoken.md).

> ❗ **Important**: Don’t declare new conformances to MetadataCollection. Only the types provided by the USDStageKit framework are valid conforming types.

## Topics

### Instance Properties
- [var allAuthoredMetadata: Dictionary<USDToken, USDValue>](usdstage-4sfi1/object/metadatacollection/allauthoredmetadata.md)
- [var allMetadata: Dictionary<USDToken, USDValue>](usdstage-4sfi1/object/metadatacollection/allmetadata.md)
- [var assetInfo: Dictionary<String, USDValue>](usdstage-4sfi1/object/metadatacollection/assetinfo.md)
- [var customData: Dictionary<String, USDValue>](usdstage-4sfi1/object/metadatacollection/customdata.md)
- [var displayName: String](usdstage-4sfi1/object/metadatacollection/displayname.md)
- [var documentation: String](usdstage-4sfi1/object/metadatacollection/documentation.md)
- [var hasAssetInfo: Bool](usdstage-4sfi1/object/metadatacollection/hasassetinfo.md)
- [var hasAuthoredAssetInfo: Bool](usdstage-4sfi1/object/metadatacollection/hasauthoredassetinfo.md)
- [var hasAuthoredCustomData: Bool](usdstage-4sfi1/object/metadatacollection/hasauthoredcustomdata.md)
- [var hasAuthoredDisplayName: Bool](usdstage-4sfi1/object/metadatacollection/hasauthoreddisplayname.md)
- [var hasAuthoredDocumentation: Bool](usdstage-4sfi1/object/metadatacollection/hasauthoreddocumentation.md)
- [var hasAuthoredHidden: Bool](usdstage-4sfi1/object/metadatacollection/hasauthoredhidden.md)
- [var hasCustomData: Bool](usdstage-4sfi1/object/metadatacollection/hascustomdata.md)
- [var isHidden: Bool](usdstage-4sfi1/object/metadatacollection/ishidden.md)
### Instance Methods
- [func assetInfoByKey(USDToken) -> USDValue?](usdstage-4sfi1/object/metadatacollection/assetinfobykey(_:).md)
- [func clearAssetInfo()](usdstage-4sfi1/object/metadatacollection/clearassetinfo.md)
- [func clearAssetInfoByKey(USDToken)](usdstage-4sfi1/object/metadatacollection/clearassetinfobykey(_:).md)
- [func clearCustomData()](usdstage-4sfi1/object/metadatacollection/clearcustomdata.md)
- [func clearCustomDataByKey(USDToken)](usdstage-4sfi1/object/metadatacollection/clearcustomdatabykey(_:).md)
- [func clearDisplayName()](usdstage-4sfi1/object/metadatacollection/cleardisplayname.md)
- [func clearDocumentation()](usdstage-4sfi1/object/metadatacollection/cleardocumentation.md)
- [func clearHidden()](usdstage-4sfi1/object/metadatacollection/clearhidden.md)
- [func clearMetadata(USDToken) throws](usdstage-4sfi1/object/metadatacollection/clearmetadata(_:).md)
- [func clearMetadata(USDToken, keyPath: USDToken) throws](usdstage-4sfi1/object/metadatacollection/clearmetadata(_:keypath:).md)
- [func customDataByKey(USDToken) -> USDValue?](usdstage-4sfi1/object/metadatacollection/customdatabykey(_:).md)
- [func hasAssetInfoByKey(USDToken) -> Bool](usdstage-4sfi1/object/metadatacollection/hasassetinfobykey(_:).md)
- [func hasAuthoredAssetInfoByKey(USDToken) -> Bool](usdstage-4sfi1/object/metadatacollection/hasauthoredassetinfobykey(_:).md)
- [func hasAuthoredCustomDataByKey(USDToken) -> Bool](usdstage-4sfi1/object/metadatacollection/hasauthoredcustomdatabykey(_:).md)
- [func hasAuthoredMetadata(USDToken) -> Bool](usdstage-4sfi1/object/metadatacollection/hasauthoredmetadata(_:).md)
- [func hasAuthoredMetadata(USDToken, keyPath: USDToken) -> Bool](usdstage-4sfi1/object/metadatacollection/hasauthoredmetadata(_:keypath:).md)
- [func hasCustomDataByKey(USDToken) -> Bool](usdstage-4sfi1/object/metadatacollection/hascustomdatabykey(_:).md)
- [func hasMetadata(USDToken) -> Bool](usdstage-4sfi1/object/metadatacollection/hasmetadata(_:).md)
- [func hasMetadata(USDToken, keyPath: USDToken) -> Bool](usdstage-4sfi1/object/metadatacollection/hasmetadata(_:keypath:).md)
- [func metadata<T>(USDToken) -> T?](usdstage-4sfi1/object/metadatacollection/metadata(_:).md)
- [func metadata<T>(USDToken, keyPath: USDToken) -> T?](usdstage-4sfi1/object/metadatacollection/metadata(_:keypath:).md)
- [func setAssetInfoByKey(USDToken, value: USDValue)](usdstage-4sfi1/object/metadatacollection/setassetinfobykey(_:value:).md)
- [func setMetadata<T>(USDToken, keyPath: USDToken, value: T) throws](usdstage-4sfi1/object/metadatacollection/setmetadata(_:keypath:value:).md)
- [func setMetadata<T>(USDToken, value: T) throws](usdstage-4sfi1/object/metadatacollection/setmetadata(_:value:).md)

## Relationships

### Conforming Types
- [USDPrim](usdprim.md)
- [USDPrim.Attribute](usdprim/attribute.md)
- [USDPrim.Property](usdprim/property.md)
- [USDPrim.Relationship](usdprim/relationship.md)
- [USDStage.Object](usdstage-4sfi1/object.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage-4sfi1/object/metadatacollection)*