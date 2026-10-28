# Get Supported Countries or Regions

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches supported languages and language codes.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)

## Discussion

Use this endpoint to fetch supported product page languages for countries or regions.

### Payload example 1: Get supported countries or regions

**Request**:

```
GET https://api.searchads.apple.com/api/v5/countries-or-regions?countriesOrRegions=US,AU,GB,CA
```

**Response**:

```json
{
   "data": [
        {
            "countryOrRegion": “US”,
            "supportedLanguages": [
                {
                    "language": "en",
                    "languageCode": "en-US"
                },
                {
                    "language": “es”,
                    "languageCode": "es-MX"
                }
            ],
            "defaultLanguage": {
                "language": "en",
                "languageCode": "en-US"
            }
        },
        {
            "countryOrRegion": "AU",
            "supportedLanguages": [
                {
                    "language": "en",
                    "languageCode": "en-AU"
                },
                {
                    "language": "en",
                    "languageCode": "en-GB"
                }
            ],
            "defaultLanguage": {
                "language": "en",
                "languageCode": "en-AU"
            }
        },
        {
            "countryOrRegion": "GB",
            "supportedLanguages": [
                {
                    "language": "en",
                    "languageCode": "en-GB"
                }
            ],
            "defaultLanguage": {
                "language": "en",
                "languageCode": "en-GB"
            }
        },
        {
            "countryOrRegion": "CA",
            "supportedLanguages": [
                {
                    "language": "en",
                    "languageCode": "en-CA"
                },
                {
                    "language”: "fr",
                    "languageCode": "fr-CA"
                }
            ],
            "defaultLanguage": {
                "language": "en",
                "languageCode": "en-CA"
            }
        }
    ]
}
```

### Payload example 2: Get supported countries or regions

**Request**:

```
GET https://api.searchads.apple.com/api/v5/countries-or-regions?countriesOrRegions=CA
```

**Response**:

```json
{
  "countryOrRegion": "CA",
  "supportedLocales": [
    {
      "language": "en",
      "languageCode": "en-CA"
    },
    {
      "language": "fr",
      "languageCode": "fr-CA"
    }
  ],
  "defaultLanguages": [
    {
      "language": "en",
      "languageCode": "en-CA"
    },
    {
      "language": "fr",
      "languageCode": "fr-CA"
    }
  ]
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/countries-or-regions`

## Parameters

### Query Parameters

- `countriesOrRegions` (string): Filters by ISO alpha-2 country codes using one or more comma-separated values. For example, use `https://api.searchads.apple.com/api/v5/countries-or-regions?countriesOrRegions=US` for a single country or region, or `https://api.searchads.apple.com/api/v5/countries-or-regions?countriesOrRegions=US,` `MX` for multiple countries or regions.

## Responses

- `200` OK (`CountriesOrRegionsListResponse`, `application/json`): If the call succeeds, the API returns the [`CountriesOrRegionsListResponse`](./countriesorregionslistresponse.md) object in the response payload with an HTTP status code of `200(OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `400` Bad Request (`ApiErrorResponse`, `application/json`): An invalid query or missing required parameters.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Product Page Endpoints
- [Get Product Pages](./get-product-pages.md)
  Fetches metadata of all your custom product pages.
- [Get Product Pages by Identifier](./get-product-pages-by-identifier.md)
  Fetches metadata for a specific product page.
- [Get Product Page Locales](./get-product-page-locales.md)
  Fetches product page locales by identifier.
- [Get App Preview Device Sizes](./get-app-preview-device-sizes.md)
  Fetches supported app preview device-size mappings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-supported-countries-or-regions)*