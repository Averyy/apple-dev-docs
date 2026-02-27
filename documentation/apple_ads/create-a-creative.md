# Create a Creative

**Framework**: Apple Ads  
**Kind**: httpRequest

Creates a creative object within an organization.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to create a [`Creative`](creative.md) object within your organization using your `productPageId`.

##### Payload Example Create a Creative

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/creatives

{
  "adamId": 899247964,
  "name": "Trip Trek CPP variation",
  "type”: "CUSTOM_PRODUCT_PAGE",
  "productPageId": "45812c9b-c296-43d3-c6a0-c5a02f74bf6e"
}
```

**Response**:

```json
{
    "id": 94895512,
    "orgId": 39872140,
    "adamId": 899247964,
    "name": "Trip Trek CPP variation",
    "type": "CUSTOM_PRODUCT_PAGE",
    "state": "VALID",
    "stateReasons": [],
    "creationTime": "2024-10-09T06:48:22.812Z",
    "modificationTime": "2024-107-09T06:48:22.812Z",
    "productPageId": "45812c9b-c296-43d3-c6a0-c5a02f74bf6e"
  }

```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/creatives`

## Request Body

The request body that includes details of the [`Creative`](creative.md).

## See Also

- [Find Creatives](find-creatives.md)
  Finds creatives within an organization.
- [Get a Creative](get-a-creative.md)
  Fetches a creative by identifier.
- [Get All Creatives](get-all-creatives.md)
  Fetches all creatives within an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/create-a-creative)*