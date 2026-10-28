# Query Supported App Languages

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Query countries and regions to discover the ad-supported languages available in each market.

**Availability**:
- Apple Ads Platform API 1.0+

## Discussion

This endpoint returns a list of countries and regions along with the languages supported for Apple Ads in each market, including each market’s `adsSupportedLanguages` and `adsDefaultLanguages`.

Use this endpoint to:

- Validate locale codes before setting them on creatives or ad groups. The API supports only a subset of ISO 639-1 languages, so treat this response as the source of truth for valid values.
- Populate country/language selection UI in campaign setup workflows.
- Confirm which languages are available when expanding campaigns into new markets.

An empty request body returns all supported countries and regions with default pagination. To scope results to specific country codes, use `filters`. To order results alphabetically, use `sorting`.

See [`QueryFilterOperator`](./queryfilteroperator.md) for the full set of supported comparison operators.

### Filterable Fields

| Field | Type | Operators | Sortable | Description |
| --- | --- | --- | --- | --- |
| `countryCode` | string | `EQUALS`, `NOT_EQUALS`, `IN` | Yes | ISO 3166-1 alpha-2 country code (for example, `US`, `GB`, `CA`) |
| `name` | string | `EQUALS`, `NOT_EQUALS`, `IN`, `STARTS_WITH`, `ENDS_WITH`, `LIKE` | Yes | Full country or region name |

The request body is a [`QueryRequest`](./queryrequest.md) composed of [`QueryFilter`](./queryfilter.md) conditions and [`QuerySort`](./querysort.md) directives ([`QuerySortOrder`](./querysortorder.md)), controlled by [`QueryPagination`](./querypagination.md).

Each result row includes the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Full display name of the country or region (for example, `United States`) |
| `countryCode` | string | ISO 3166-1 alpha-2 code (for example, `US`) |
| `adsSupportedLanguages` | array | All language/locale combinations eligible for Apple Ads creatives and targeting in this market |
| `adsDefaultLanguages` | array | The default language(s) used when no explicit locale is specified |
| `adsSupportedLanguages[].language` | string | Language identifier, usually an ISO 639-1 code (for example, `en`, `es`, `fr`). Can be another standard, such as `yue` (ISO 639-3) |
| `adsSupportedLanguages[].languageCode` | string | BCP-47 locale code with a region or script subtag (for example, `en-US`, `es-MX`, `zh-Hans`) |

## Payload Examples

**All Countries**:

Return all supported countries and regions sorted alphabetically by name. Useful for populating a full country/language picker in a campaign setup UI.

### Request

```http
POST /v1/metadata/apps/supported-languages/query

{
 "sorting": [
   { "field": "name", "order": "ASC" }
 ],
 "pagination": { "offset": 0, "pageSize": 100 }
}
```

### Response

```json
{
 "result": [
   {
     "name": "Australia",
     "countryCode": "AU",
     "adsSupportedLanguages": [
       {
         "language": "en",
         "languageCode": "en-AU"
       }
     ],
     "adsDefaultLanguages": [
       {
         "language": "en",
         "languageCode": "en-AU"
       }
     ]
   },
   {
     "name": "Canada",
     "countryCode": "CA",
     "adsSupportedLanguages": [
       {
         "language": "en",
         "languageCode": "en-CA"
       },
       {
         "language": "fr",
         "languageCode": "fr-CA"
       }
     ],
     "adsDefaultLanguages": [
       {
         "language": "en",
         "languageCode": "en-CA"
       }
     ]
   },
   {
     "name": "United States",
     "countryCode": "US",
     "adsSupportedLanguages": [
       {
         "language": "en",
         "languageCode": "en-US"
       },
       {
         "language": "es",
         "languageCode": "es-MX"
       },
       {
         "language": "zh",
         "languageCode": "zh-Hans"
       }
     ],
     "adsDefaultLanguages": [
       {
         "language": "en",
         "languageCode": "en-US"
       }
     ]
   }
 ],
 "pagination": {
   "totalCount": 91,
   "offset": 0,
   "pageSize": 100
 }
}
```

**Filter by Country Code**:

Fetch language details for a single country by its ISO code. To confirm available locales before setting creatives or ad group targeting for a specific market, use this.

### Request

```http
POST /v1/metadata/apps/supported-languages/query

{
 "filters": [
   {
     "field": "countryCode",
     "operator": "EQUALS",
     "value": "US"
   }
 ]
}
```

### Response

```json
{
 "result": [
   {
     "name": "United States",
     "countryCode": "US",
     "adsSupportedLanguages": [
       {
         "language": "en",
         "languageCode": "en-US"
       },
       {
         "language": "es",
         "languageCode": "es-MX"
       },
       {
         "language": "zh",
         "languageCode": "zh-Hans"
       }
     ],
     "adsDefaultLanguages": [
       {
         "language": "en",
         "languageCode": "en-US"
       }
     ]
   }
 ],
 "pagination": {
   "totalCount": 1,
   "offset": 0,
   "pageSize": 100
 }
}
```

**Filter by Multiple Countries**:

Fetch language details for several countries at once. Useful when validating locales for a multi-market campaign rollout.

### Request

```http
POST /v1/metadata/apps/supported-languages/query

{
 "filters": [
   {
     "field": "countryCode",
     "operator": "IN",
     "value": ["US", "GB", "CA", "AU"]
   }
 ],
 "sorting": [
   { "field": "name", "order": "ASC" }
 ]
}
```

### Response

```json
{
 "result": [
   {
     "name": "Australia",
     "countryCode": "AU",
     "adsSupportedLanguages": [
       {
         "language": "en",
         "languageCode": "en-AU"
       }
     ],
     "adsDefaultLanguages": [
       {
         "language": "en",
         "languageCode": "en-AU"
       }
     ]
   },
   {
     "name": "Canada",
     "countryCode": "CA",
     "adsSupportedLanguages": [
       {
         "language": "en",
         "languageCode": "en-CA"
       },
       {
         "language": "fr",
         "languageCode": "fr-CA"
       }
     ],
     "adsDefaultLanguages": [
       {
         "language": "en",
         "languageCode": "en-CA"
       }
     ]
   },
   {
     "name": "United Kingdom",
     "countryCode": "GB",
     "adsSupportedLanguages": [
       {
         "language": "en",
         "languageCode": "en-GB"
       }
     ],
     "adsDefaultLanguages": [
       {
         "language": "en",
         "languageCode": "en-GB"
       }
     ]
   },
   {
     "name": "United States",
     "countryCode": "US",
     "adsSupportedLanguages": [
       {
         "language": "en",
         "languageCode": "en-US"
       },
       {
         "language": "es",
         "languageCode": "es-MX"
       },
       {
         "language": "zh",
         "languageCode": "zh-Hans"
       }
     ],
     "adsDefaultLanguages": [
       {
         "language": "en",
         "languageCode": "en-US"
       }
     ]
   }
 ],
 "pagination": {
   "totalCount": 4,
   "offset": 0,
   "pageSize": 100
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/metadata/apps/supported-languages/query`

## Parameters

### Header Parameters

- `X-AP-Context` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `QueryRequest`

## Responses

- `200` OK (`AppSupportedLanguagesQueryResponse`, `application/json`)
- `400` Bad Request (`AppSupportedLanguagesQueryResponse`, `application/json`)
- `401` Unauthorized (`Error`, `application/json`)
- `403` Forbidden (`Error`, `application/json`)
- `404` Not Found (`Error`, `application/json`)
- `429` Too Many Requests (`Error`, `application/json`)
- `500` Internal Server Error (`Error`, `application/json`)

## See Also

- [Search for Apps](./searches-for-a-list-of-apps.md)
  Search the App Store for apps matching the supplied criteria and return app details.
- [Get App Details by Adam ID](./get-app-details-by-adam-id.md)
  Retrieve application details for a specific Adam ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-supported-app-languages)*