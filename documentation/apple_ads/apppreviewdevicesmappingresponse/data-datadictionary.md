# AppPreviewDevicesMappingResponse.Data

**Framework**: Apple Ads  
**Kind**: dictionary

The app preview device mapping to display name and size mapping.

**Availability**:
- Search Ads 2.0.9+

## Declaration

```swift
object AppPreviewDevicesMappingResponse.Data
```

## Properties

- `Any Key` (string): A map of app preview device sizes. The key is the identifier and the value is the display name. You can also use this to define the supported fallback devices if mapping isn’t available. ```json
{
  "ipadPro": "iPad 12.9",
  "iphone6+": "iPhone 5.5",
  "iphone_5_8": "iPhone 5.8",
  "iphone5": "iPhone 4",
  "iphone6": "iPhone 4.7",
  "ipadPro_2018": "iPad 11",
  "ipad": "iPad 9.7",
  "iphone_6_5": "iPhone 6.5",
  "ipad_10_5": "iPad 10.5"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/apppreviewdevicesmappingresponse/data-data.dictionary)*