# Find Creatives

**Framework**: Apple Ads  
**Kind**: httpRequest

Finds creatives within an organization.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to find creatives using a [`Selector`](selector.md) [`Condition`](condition.md) to filter results. If you don’t specify selector conditions, all creatives return in the response. See [`Creative`](creative.md) for field descriptions and selector condition operators.

Values are case-sensitive strings. The `orderBy` selector supports the `Id` and `name` fields.

##### Payload Example Find Creatives

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/creatives/find

{
  "conditions": [
    {
      "field": "name",
      "operator": "CONTAINS",
      "values": [
        "Trip"
      ]
    }
  ]
}

```

**Response**:

```json
{
  "data": [
    {
      "id": 573408745,
      "orgId": 39872140,
      "adamId": 899247664,
      "name": "Trip Trek custom product page variation 1",
      "type": "CUSTOM_PRODUCT_PAGE",
      "state": "VALID",
      "stateReasons": [],
      "creationTime": "2024-10-09T20:07:19.506Z",
      "modificationTime": "2024-10-18T20:07:19.506Z",
      "productPageId": "76659d7a-d146-43d3-b6b8-b7a12f74bf6b"
    },
    {
      "id": 75606108,
      "orgId": 39879640,
      "adamId": 1004806037,
      "name": "Trip Trek Creative Set variation 2",
      "type": "CREATIVE_SET",
      "state": "INVALID",
      "stateReasons": [],
      "creationTime": "2024-03-04T02:44:14.775",
      "modificationTime": "2024-08-17T01:16:37.827",
      "languageCode": "en_US"
    }
  ],
  “pagination”: {
    “totalResults”: 2,
    “startIndex”: 1,
    “itemsPerPage”: 10
  }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/creatives/find`

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.

## See Also

- [Create a Creative](create-a-creative.md)
  Creates a creative object within an organization.
- [Get a Creative](get-a-creative.md)
  Fetches a creative by identifier.
- [Get All Creatives](get-all-creatives.md)
  Fetches all creatives within an organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-creatives)*