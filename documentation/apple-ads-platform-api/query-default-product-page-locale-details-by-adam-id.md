# Query App Locale Details

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Return the default product page locale details for an app identified by its adamId.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns the default product page locale details for an app identified by its `adamId`. The default product page represents the app’s main App Store listing: the page that all users see unless directed to a custom product page.

In App Store Connect, there is no explicit “default product page” entity. The app’s main listing is the default. This endpoint surfaces that listing through the same `AppLocaleDetails` structure, so the response format is consistent across both endpoints.

To quickly fetch the default page content for an app without needing to first look up the product page ID, use this endpoint. Each object in the result corresponds to one supported language for the default product page.

Keep the following constraints in mind when querying default locale details:

| Constraint | Detail |
| --- | --- |
| Default page only | This endpoint returns only the default product page. Custom product pages require the Query Product Page Locale Details endpoint. |
| All locales returned | This endpoint returns all locales configured for the default product page. Filter by `languageCode` in the request body `filters` array if you need a specific locale. |
| assetsByDevice structure | The `assetsByDevice` field maps each specific device type (e.g., `iphone_6_5`, `iphone_6_7`) to a `DeviceAssetGroup` containing an `assets` array of asset references and an `appPreviewDeviceFallBackDevices` array. |

#### Payload Examples

##### Request

Returns the default product page locale details for an app identified by its `adamId`. The default product page represents the app’s main App Store listing: the page that all users see unless directed to a custom product page.

```None
POST https://api.ads.apple.com/v1/apps/123456789/locale-details/query
```

##### Response

```json
{
 "result": [
   {
     "adamId": 123456789,
     "language": "en",
     "languageCode": "en-US",
     "isPrimaryLocale": true,
     "appName": "AwayFinder",
     "subTitle": "Find your next adventure",
     "promotionalText": "Now with personalized travel recommendations",
     "shortDescription": "The all-in-one travel discovery app.",
     "deviceClasses": [
       "IPHONE",
       "IPAD"
     ],
     "assetsByDevice": {
       "iphone_6_5": {
         "assets": [
           {
             "assetId": "41a91e19-e021-45bb-ac5a-5faec02f9445"
           },
           {
             "assetId": "52b02f2a-f132-56cc-bd6b-6gbfd13g0556"
           }
         ],
         "appPreviewDeviceFallBackDevices": []
       },
       "iphone_6_7": {
         "assets": [
           {
             "assetId": "63c13g3b-g243-67dd-ce7c-7hcge24h1667"
           }
         ],
         "appPreviewDeviceFallBackDevices": [
           "iphone_6_5"
         ]
       }
     }
   },
   {
     "adamId": 123456789,
     "language": "fr",
     "languageCode": "fr-FR",
     "isPrimaryLocale": false,
     "appName": "AwayFinder",
     "subTitle": "Trouvez votre prochaine aventure",
     "promotionalText": "Avec des recommandations de voyage personnalisées",
     "shortDescription": "L'application de découverte de voyages tout-en-un.",
     "deviceClasses": [
       "IPHONE"
     ],
     "assetsByDevice": {
       "iphone_6_5": {
         "assets": [
           {
             "assetId": "c5c641c8-026a-44fb-a3ce-0f78cab73cad"
           }
         ],
         "appPreviewDeviceFallBackDevices": []
       }
     }
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/apps/{adamId}/locale-details/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Product Pages](query-product-pages.md)
  Queries App Store product pages available to your account.
- [Get Product Page by ID](get-product-page-by-id.md)
  Retrieves a specific Product Page (DPP, CPP, or PPO) by its unique UUID.
- [Query Product Page Locale Details](query-product-page-locale-details.md)
  Queries the localized content associated with a custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-default-product-page-locale-details-by-adam-id)*