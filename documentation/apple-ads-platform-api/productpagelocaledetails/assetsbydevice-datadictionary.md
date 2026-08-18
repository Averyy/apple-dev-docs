# ProductPageLocaleDetails.AssetsByDevice

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A map of device type to a `DeviceAssetGroup` object.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ProductPageLocaleDetails.AssetsByDevice
```

#### Discussion

Each key is a device type identifier, such as `iphone_6_5` or `iphone_6_7`, not a fixed field name. `assetsByDevice` is a free-form map rather than an object with named properties, so the reference page labels this key `Any Key`. The value for each key is a [`DeviceAssetGroup`](deviceassetgroup.md) containing that device’s asset references and fallback devices.

On the parent [`ProductPageLocaleDetails`](productpagelocaledetails.md) object, `assetsByDevice` is the field that carries a product page locale’s screenshots and preview videos. Each device-type key maps to a [`DeviceAssetGroup`](deviceassetgroup.md) holding an `assets` array of asset references and an `appPreviewDeviceFallBackDevices` array listing which other device types to fall back to when assets are not available for that class.

## Properties

- `Any Key` (DeviceAssetGroup)


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/productpagelocaledetails/assetsbydevice-data.dictionary)*