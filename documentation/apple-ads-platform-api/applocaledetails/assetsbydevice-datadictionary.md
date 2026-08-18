# AppLocaleDetails.AssetsByDevice

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Map of device type to a `DeviceAssetGroup` containing the ordered list of asset IDs and any fallback device references.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppLocaleDetails.AssetsByDevice
```

#### Discussion

Each key is a device type identifier, such as `iphone_6_5` or `iphone_6_7`, not a fixed field name. `assetsByDevice` is a free-form map rather than an object with named properties, so the reference page labels this key `Any Key`. The value for each key is a [`DeviceAssetGroup`](deviceassetgroup.md).

On the parent [`AppLocaleDetails`](applocaledetails.md) object, `assetsByDevice` maps each device type to a `DeviceAssetGroup` containing the ordered list of asset IDs and any fallback device references for that locale’s Default Product Page content.

## Properties

- `Any Key` (DeviceAssetGroup)


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/applocaledetails/assetsbydevice-data.dictionary)*