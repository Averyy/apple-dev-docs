# ProductPageLocaleDetails

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Locale-specific metadata for an App Store product page.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ProductPageLocaleDetails
```

#### Discussion

`ProductPageLocaleDetails` provides the locale-specific content for an App Store product page, including display text and creative assets organized by device type. Each record is tied to a specific `languageCode`, making it possible to retrieve the exact creative content users will see in a given locale.

The `assetsByDevice` map is the primary structure for accessing locale media.

##### Example

```json
{
  "adamId": 324684580,
  "language": "en",
  "languageCode": "en-US",
  "appName": "AwayFinder - Travel Planner",
  "subTitle": "Plan your next getaway",
  "promotionalText": "Get 3 months of Premium free",
  "shortDescription": "Discover, plan, and book trips with AwayFinder's curated travel guides.",
  "deviceClasses": [
    "IPHONE",
    "IPAD"
  ],
  "assetsByDevice": {
    "iphone_6_5": {
      "assets": [
        {
          "assetId": "550e8400-e29b-41d4-a716-446655440000"
        }
      ],
      "appPreviewDeviceFallBackDevices": [
        "iphone_6_7"
      ]
    },
    "iphone_6_7": {
      "assets": [
        {
          "assetId": "661f9511-f3ac-52e5-b827-557766551111"
        }
      ],
      "appPreviewDeviceFallBackDevices": []
    }
  },
  "productPageId": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc"
}
```

## Topics

### Dictionaries
- [object ProductPageLocaleDetails.AssetsByDevice](productpagelocaledetails/assetsbydevice-data.dictionary.md)
  A map of device type to a `DeviceAssetGroup` object.

## Properties

- `adamId` (int64): The app’s Adam ID. The unique App Store identifier for the promoted object. Used as promotedObjectId when creating a campaign.
- `language` (string): The language identifier, e.g. en.
- `languageCode` (string): The BCP-47 language code, e.g. en-US.
- `appName` (string): The localized application display name as it appears on the App Store.
- `subTitle` (string): The app subtitle for the locale.
- `promotionalText` (string): The promotional text for the locale. Max 170 characters.
- `shortDescription` (string): A short description for the locale. Max 4000 characters.
- `deviceClasses` ([string]): Supported device classes. Use to verify targeting compatibility when configuring ad groups with device-class targeting. Possible values: `IPHONE`, `IPAD`.
- `assetsByDevice` (ProductPageLocaleDetails.AssetsByDevice): Map of device type (e.g., `iphone_6_5`, `iphone_6_7`) to a [`DeviceAssetGroup`](deviceassetgroup.md) object. Keys are specific device type strings, not limited to the values in `deviceClasses`.
- `productPageId` (string): The parent product page identifier (ASC product page ID).

## See Also

- [object ProductPageDetails](productpagedetails.md)
  Product page metadata for a Default Product Page, Custom Product Page, or Product Page Optimization (PPO) variant.
- [object ProductPageDetailsResponse](productpagedetailsresponse.md)
  Response object for a single product page retrieval.
- [object ProductPageDetailsQueryResponse](productpagedetailsqueryresponse.md)
  Paginated response object for the product page details query.
- [object ProductPageLocaleDetailsQueryResponse](productpagelocaledetailsqueryresponse.md)
  Paginated response object for the product page locale details query.
- [object DeviceAssetGroup](deviceassetgroup.md)
  Represents assets organized by device type with fallback device information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/productpagelocaledetails)*