# Get All Creatives

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches all creatives within an organization.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to fetch details of all assigned [`Creative`](creative.md) objects for your organization.

##### Payload Example Get All Creatives

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/creatives
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

`GET https://api.searchads.apple.com/api/v5/creatives`

## Parameters

- `limit` (int32): The number of items to return per request. The maximum is 1000 for most objects.
- `offset` (int32): The offset pagination that limits the number of returned records. The start of each page is offset by the specified number.

## See Also

- [Create a Creative](create-a-creative.md)
  Creates a creative object within an organization.
- [Find Creatives](find-creatives.md)
  Finds creatives within an organization.
- [Get a Creative](get-a-creative.md)
  Fetches a creative by identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-all-creatives)*