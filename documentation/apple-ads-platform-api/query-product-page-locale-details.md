# Query Product Page Locale Details

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Queries the localized content associated with a custom product page.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint queries the localized content associated with a specific product page. For each language version, the response returns the metadata that Apple Ads will show (including the localized `appName`, `subTitle`, `promotionalText`, and `shortDescription`) along with asset references organized by device class in the `assetsByDevice` field.

To preview how a product page creative will appear across different locales before using it in a campaign, use this endpoint. This is especially useful when managing multi-locale campaigns to verify that all required language variants are present and correctly populated.

The endpoint requires a filter on `productPageId`. Omitting the `languageCode` filter returns locale details for all supported languages of the product page. Add a `languageCode` filter to retrieve a specific locale.

#### Request Body

The `filters` array supports the following fields:

| Field | Supported Operators | Notes |
| --- | --- | --- |
| `productPageId` | `EQUALS` | Scopes the query to a specific product page. See Key Constraints below. |
| `language` | `EQUALS` | Filter to a specific language identifier, such as `en` or `fr`. |
| `languageCode` | `EQUALS` | Filter to a specific locale, such as `en-US` or `fr-FR`. |

Keep the following constraints in mind when querying locale details:

| Constraint | Detail |
| --- | --- |
| productPageId required | A filter on `productPageId` is required. The query will return an error without it. |
| All locales by default | Omitting `languageCode` returns all locales configured for the product page. |
| assetsByDevice structure | The `assetsByDevice` field maps each specific device type (e.g., `iphone_6_5`, `iphone_6_7`) to a `DeviceAssetGroup` containing an `assets` array of asset references and an `appPreviewDeviceFallBackDevices` array. |

#### Payload Examples

**All Locales for a Page**:

##### Request

```json
{
 "filters": [
   {
     "field": "productPageId",
     "operator": "EQUALS",
     "value": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc"
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "productPageId": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
     "adamId": 123456789,
     "language": "en",
     "languageCode": "en-US",
     "appName": "AwayFinder",
     "subTitle": "Get more done every day",
     "promotionalText": "Now with AI-powered scheduling",
     "shortDescription": "The all-in-one task manager for busy professionals.",
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
       }
     }
   },
   {
     "productPageId": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
     "adamId": 123456789,
     "language": "fr",
     "languageCode": "fr-FR",
     "appName": "AwayFinder",
     "subTitle": "Accomplissez plus chaque jour",
     "promotionalText": "Maintenant avec planification par IA",
     "shortDescription": "Le gestionnaire de tâches tout-en-un.",
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

**Specific Language**:

##### Request

```json
{
 "filters": [
   {
     "field": "productPageId",
     "operator": "EQUALS",
     "value": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc"
   },
   {
     "field": "languageCode",
     "operator": "EQUALS",
     "value": "en-US"
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "productPageId": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
     "adamId": 123456789,
     "language": "en",
     "languageCode": "en-US",
     "appName": "AwayFinder",
     "subTitle": "Get more done every day",
     "promotionalText": "Now with AI-powered scheduling",
     "shortDescription": "The all-in-one task manager for busy professionals.",
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
             "assetId": "9ea4bb81-5f18-401f-bfe1-101a6ee6d328"
           }
         ],
         "appPreviewDeviceFallBackDevices": [
           "iphone_6_5"
         ]
       }
     }
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/product-pages/locale-details/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

See [`QueryRequest`](queryrequest.md).

## See Also

- [Query Product Pages](query-product-pages.md)
  Queries App Store product pages available to your account.
- [Get Product Page by ID](get-product-page-by-id.md)
  Retrieves a specific Product Page (DPP, CPP, or PPO) by its unique UUID.
- [Query App Locale Details](query-default-product-page-locale-details-by-adam-id.md)
  Return the default product page locale details for an app identified by its adamId.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-product-page-locale-details)*