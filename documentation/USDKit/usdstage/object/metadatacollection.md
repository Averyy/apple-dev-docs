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
- [var allAuthoredMetadata: Dictionary<USDToken, USDValue>](usdstage/object/metadatacollection/allauthoredmetadata.md)
- [var allMetadata: Dictionary<USDToken, USDValue>](usdstage/object/metadatacollection/allmetadata.md)
- [var assetInfo: Dictionary<String, USDValue>](usdstage/object/metadatacollection/assetinfo.md)
- [var customData: Dictionary<String, USDValue>](usdstage/object/metadatacollection/customdata.md)
- [var displayName: String](usdstage/object/metadatacollection/displayname.md)
- [var documentation: String](usdstage/object/metadatacollection/documentation.md)
- [var hasAssetInfo: Bool](usdstage/object/metadatacollection/hasassetinfo.md)
- [var hasAuthoredAssetInfo: Bool](usdstage/object/metadatacollection/hasauthoredassetinfo.md)
- [var hasAuthoredCustomData: Bool](usdstage/object/metadatacollection/hasauthoredcustomdata.md)
- [var hasAuthoredDisplayName: Bool](usdstage/object/metadatacollection/hasauthoreddisplayname.md)
- [var hasAuthoredDocumentation: Bool](usdstage/object/metadatacollection/hasauthoreddocumentation.md)
- [var hasAuthoredHidden: Bool](usdstage/object/metadatacollection/hasauthoredhidden.md)
- [var hasCustomData: Bool](usdstage/object/metadatacollection/hascustomdata.md)
- [var isHidden: Bool](usdstage/object/metadatacollection/ishidden.md)
### Instance Methods
- [func assetInfoByKey(USDToken) -> USDValue?](usdstage/object/metadatacollection/assetinfobykey(_:).md)
- [func clearAssetInfo()](usdstage/object/metadatacollection/clearassetinfo.md)
- [func clearAssetInfoByKey(USDToken)](usdstage/object/metadatacollection/clearassetinfobykey(_:).md)
- [func clearCustomData()](usdstage/object/metadatacollection/clearcustomdata.md)
- [func clearCustomDataByKey(USDToken)](usdstage/object/metadatacollection/clearcustomdatabykey(_:).md)
- [func clearDisplayName()](usdstage/object/metadatacollection/cleardisplayname.md)
- [func clearDocumentation()](usdstage/object/metadatacollection/cleardocumentation.md)
- [func clearHidden()](usdstage/object/metadatacollection/clearhidden.md)
- [func clearMetadata(USDToken) throws](usdstage/object/metadatacollection/clearmetadata(_:).md)
- [func clearMetadata(USDToken, keyPath: USDToken) throws](usdstage/object/metadatacollection/clearmetadata(_:keypath:).md)
- [func customDataByKey(USDToken) -> USDValue?](usdstage/object/metadatacollection/customdatabykey(_:).md)
- [func hasAssetInfoByKey(USDToken) -> Bool](usdstage/object/metadatacollection/hasassetinfobykey(_:).md)
- [func hasAuthoredAssetInfoByKey(USDToken) -> Bool](usdstage/object/metadatacollection/hasauthoredassetinfobykey(_:).md)
- [func hasAuthoredCustomDataByKey(USDToken) -> Bool](usdstage/object/metadatacollection/hasauthoredcustomdatabykey(_:).md)
- [func hasAuthoredMetadata(USDToken) -> Bool](usdstage/object/metadatacollection/hasauthoredmetadata(_:).md)
- [func hasAuthoredMetadata(USDToken, keyPath: USDToken) -> Bool](usdstage/object/metadatacollection/hasauthoredmetadata(_:keypath:).md)
- [func hasCustomDataByKey(USDToken) -> Bool](usdstage/object/metadatacollection/hascustomdatabykey(_:).md)
- [func hasMetadata(USDToken) -> Bool](usdstage/object/metadatacollection/hasmetadata(_:).md)
- [func hasMetadata(USDToken, keyPath: USDToken) -> Bool](usdstage/object/metadatacollection/hasmetadata(_:keypath:).md)
- [func metadata(USDToken) -> UInt?](usdstage/object/metadatacollection/metadata(_:)-136hk.md)
- [func metadata<T>(USDToken) -> T?](usdstage/object/metadatacollection/metadata(_:)-2wkc9.md)
- [func metadata(USDToken) -> Int?](usdstage/object/metadatacollection/metadata(_:)-8jz5b.md)
- [func metadata(USDToken, keyPath: USDToken) -> UInt?](usdstage/object/metadatacollection/metadata(_:keypath:)-5pid3.md)
- [func metadata(USDToken, keyPath: USDToken) -> Int?](usdstage/object/metadatacollection/metadata(_:keypath:)-8isq8.md)
- [func metadata<T>(USDToken, keyPath: USDToken) -> T?](usdstage/object/metadatacollection/metadata(_:keypath:)-ngj2.md)
- [func setAssetInfoByKey(USDToken, value: USDValue)](usdstage/object/metadatacollection/setassetinfobykey(_:value:).md)
- [func setMetadata(USDToken, keyPath: USDToken, value: UInt) throws](usdstage/object/metadatacollection/setmetadata(_:keypath:value:)-1ri3i.md)
- [func setMetadata<T>(USDToken, keyPath: USDToken, value: T) throws](usdstage/object/metadatacollection/setmetadata(_:keypath:value:)-2h9mx.md)
- [func setMetadata(USDToken, keyPath: USDToken, value: Int) throws](usdstage/object/metadatacollection/setmetadata(_:keypath:value:)-8isk6.md)
- [func setMetadata(USDToken, value: Int) throws](usdstage/object/metadatacollection/setmetadata(_:value:)-22f8j.md)
- [func setMetadata<T>(USDToken, value: T) throws](usdstage/object/metadatacollection/setmetadata(_:value:)-7t6dx.md)
- [func setMetadata(USDToken, value: UInt) throws](usdstage/object/metadatacollection/setmetadata(_:value:)-8hsn7.md)

## Relationships

### Conforming Types
- [USDPrim](usdprim.md)
- [USDPrim.Attribute](usdprim/attribute.md)
- [USDPrim.Property](usdprim/property.md)
- [USDPrim.Relationship](usdprim/relationship.md)
- [USDStage.Object](usdstage/object.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/object/metadatacollection)*