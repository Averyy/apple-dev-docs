# Query Supported App Languages

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query countries and regions to discover the ad-supported languages available in each market.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns a list of countries and regions along with the languages supported for Apple Ads in each market, including each market’s `adsSupportedLanguages` and `adsDefaultLanguages`.

Use this endpoint to:

- Validate locale codes before setting them on creatives or ad groups.
- Populate country/language selection UI in campaign setup workflows.
- Confirm which languages are available when expanding campaigns into new markets.

An empty request body returns all supported countries and regions with default pagination. To scope results to specific country codes, use `filters`. To order results alphabetically, use `sorting`.

The `filters` array supports the following fields:

| Field | Supported Operators | Notes |
| --- | --- | --- |
| `countryCode` | `EQUALS`, `INCLUDE` | ISO 3166-1 alpha-2 country code (e.g., `US`, `GB`, `CA`). |
| `name` | `EQUALS` | Full country or region name. |

The `sorting` array supports the following fields:

| Field | Notes |
| --- | --- |
| `name` | Sort alphabetically by country or region name. |
| `countryCode` | Sort by country code. |

Each result row includes the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Full display name of the country or region (e.g., `United States`). |
| `countryCode` | string | ISO 3166-1 alpha-2 code (e.g., `US`). |
| `adsSupportedLanguages` | array | All language/locale combinations eligible for Apple Ads creatives and targeting in this market. |
| `adsDefaultLanguages` | array | The default language(s) used when no explicit locale is specified. |
| `adsSupportedLanguages[].language` | string | Language identifier (e.g., `en`, `es`, `fr`). |
| `adsSupportedLanguages[].languageCode` | string | Full locale code (e.g., `en-US`, `es-US`). |

#### Payload Examples

**All Countries**:

Return all supported countries and regions sorted alphabetically by name. Useful for populating a full country/language picker in a campaign setup UI.

##### Request

```json
POST /v1/metadata/apps/supported-languages/query

{
 "sorting": [
   { "field": "name", "order": "ASC" }
 ],
 "pagination": { "offset": 0, "pageSize": 100 }
}
```

##### Response

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
         "languageCode": "es-US"
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

##### Request

```json
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

##### Response

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
         "languageCode": "es-US"
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

##### Request

```json
POST /v1/metadata/apps/supported-languages/query

{
 "filters": [
   {
     "field": "countryCode",
     "operator": "INCLUDE",
     "value": ["US", "GB", "CA", "AU"]
   }
 ],
 "sorting": [
   { "field": "name", "order": "ASC" }
 ]
}
```

##### Response

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
         "languageCode": "es-US"
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

- `X-Ap-Context` (string) *(required)*

## See Also

- [Search for Apps](searches-for-a-list-of-apps.md)
  Search the App Store for apps matching the supplied criteria and return app details.
- [Get App Details by Adam ID](get-app-details-by-adam-id.md)
  Retrieve application details for a specific Adam ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-supported-app-languages)*