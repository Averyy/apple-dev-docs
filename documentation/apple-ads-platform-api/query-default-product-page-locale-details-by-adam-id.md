# Query App Locale Details

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Returns the default product page locale details for an app identified by its adamId.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

The default product page is the app’s main App Store listing, the page all users see unless directed to a custom product page. This endpoint returns its localized content for an app identified by `adamId`, using the same structure as [`Query Product Page Locale Details`](./query-product-page-locale-details.md), so you don’t need a `productPageId`.

To retrieve locale details for a custom product page, see [`Query Product Page Locale Details`](./query-product-page-locale-details.md).

Each object in the result corresponds to one supported language for the default product page.

Keep the following constraints in mind when querying default locale details:

| Constraint | Detail |
| --- | --- |
| All locales returned | This endpoint returns all locales configured for the default product page. Filter by `languageCode` in the request body `filters` array if you need a specific locale. |
| assetsByDevice structure | The `assetsByDevice` field maps each specific device type (for example, `iphone_6_5`, `iphone_6_7`) to a `DeviceAssetGroup` containing an `assets` array of asset references and an `appPreviewDeviceFallBackDevices` array. |

See [`QueryFilterOperator`](./queryfilteroperator.md) for the full set of supported comparison operators.

##### Filterable Fields

| Field | Type | Operators | Sortable | Description |
| --- | --- | --- | --- | --- |
| `languageCode` | string |  |  | Filter to a specific locale, such as `en-US` or `fr-FR`. |

The `adamId` field identifies the app via the URL path (`/v1/apps/{adamId}/locale-details/query`), not a request body filter. The request body is a [`QueryRequest`](./queryrequest.md) composed of [`QueryFilter`](./queryfilter.md) conditions and [`QuerySort`](./querysort.md) directives ([`QuerySortOrder`](./querysortorder.md)), controlled by [`QueryPagination`](./querypagination.md).

#### Payload Examples

##### Request

Returns the default product page locale details for an app identified by its `adamId`. The default product page represents the app’s main App Store listing: the page that all users see unless directed to a custom product page.

```
POST /v1/apps/123456789/locale-details/query
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

### Path Parameters

- `adamId` (int64) *(required)*

### Header Parameters

- `X-AP-Context` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `QueryRequest`

## Responses

- `200` OK (`AppLocaleDetailsQueryResponse`, `application/json`)
- `400` Bad Request (`AppLocaleDetailsQueryResponse`, `application/json`)
- `401` Unauthorized (`Error`, `application/json`)
- `403` Forbidden (`Error`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` Too Many Requests (`Error`, `application/json`)
- `500` Internal Server Error (`Error`, `application/json`)

## See Also

- [Query Product Pages](./query-product-pages.md)
  Queries App Store product pages available to your account.
- [Get Product Page by ID](./get-product-page-by-id.md)
  Retrieves a specific Custom Product Page (CPP) by its unique UUID.
- [Query Product Page Locale Details](./query-product-page-locale-details.md)
  Queries the localized content of custom product pages (CPPs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-default-product-page-locale-details-by-adam-id)*