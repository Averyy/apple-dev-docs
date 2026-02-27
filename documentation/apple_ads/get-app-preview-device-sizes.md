# Get App Preview Device Sizes

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches supported app preview device-size mappings.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Creative Sets](creative-sets.md)

#### Discussion

Use this endpoint to return a complete list of supported app preview device-size mappings.

##### Payload Example Get App Preview Device Sizes

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/creativeappmappings/devices
```

**Response**:

```json
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

## Endpoint

`GET https://api.searchads.apple.com/api/v5/creativeappmappings/devices`

## See Also

- [Get Product Pages](get-product-pages.md)
  Fetches metadata of all your custom product pages.
- [Get Product Pages by Identifier](get-product-pages-by-identifier.md)
  Fetches metadata for a specific product page.
- [Get Product Page Locales](get-product-page-locales.md)
  Fetches product page locales by identifier.
- [Get Supported Countries or Regions](get-supported-countries-or-regions.md)
  Fetches supported languages and language codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-app-preview-device-sizes)*