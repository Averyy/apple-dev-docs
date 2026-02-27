# Get a Creative

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches a creative by identifier.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to fetch details of a [`Creative`](creative.md) using your `creativeId` in the resource path.

##### Payload Example Get a Creative

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/creatives/{creativeId}
```

**Response**:

```json
 {
      "id": 94790778,
      "orgId": 42173330,
      "adamId": 918469737,
      "name": "Trip Trek CPP variation 1",
      "type": "CUSTOM_PRODUCT_PAGE",
      "state": "VALID",
      "stateReasons": [],
      "creationTime": "2024-11-08T21:53:35.036",
      "modificationTime": "2024-09-04T21:53:35.036",
      "productPageId": "00d99d1e-ee93-48fc-973e-7ffc0ddfced6"
 }
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/creatives/{creativeId}`

## Parameters

- `includeDeletedCreativeSetAssets` (boolean): Include deleted assets in the response. By default deleted assets don’t return.

## See Also

- [Create a Creative](create-a-creative.md)
  Creates a creative object within an organization.
- [Find Creatives](find-creatives.md)
  Finds creatives within an organization.
- [Get All Creatives](get-all-creatives.md)
  Fetches all creatives within an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-a-creative)*