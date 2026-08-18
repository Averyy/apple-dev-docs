# Query Brands

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a paginated list of brands using filters and sorting.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns a paginated list of brands accessible to the ad account. An empty request body returns all brands with default pagination.

The brand `id` returned in results corresponds to the `promotedObjectId` used when creating `BUSINESS_BRAND` campaigns.

#### Request Body

See [`QueryRequest`](queryrequest.md).

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `filters` | array | No | Filter conditions to narrow results. |
| `sorting` | array | No | Sort order for results (field + ASC/DESC). |
| `pagination` | object | No | Offset and page size. Defaults apply if omitted. |

#### Payload Examples

**Query Brands**:

##### Request

```json
POST /v1/business-brands/query

{
 "filters": [
   {
     "field": "id",
     "operator": "EQUALS",
     "value": "9151314442816847872"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20,
   "fetchTotalCount": true
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": "9151314442816847872",
     "name": "AwayFinder",
     "countryOrRegion": "US",
     "categories": [
       "dining.restaurant"
     ],
     "eligibility": {
       "status": "ELIGIBLE"
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

**Filter by Eligibility**:

##### Request

Returns only brands you can use in a campaign. Confirm a brand’s eligibility with this filter before creating a Brands campaign, as described in [`Ads on Apple Maps Endpoints`](brands-endpoints.md).

```json
POST /v1/business-brands/query

{
 "filters": [
   {
     "field": "eligibility.status",
     "operator": "EQUALS",
     "value": "ELIGIBLE"
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "id": "9151314442816847872",
     "name": "AwayFinder",
     "countryOrRegion": "US",
     "categories": [
       "dining.restaurant"
     ],
     "eligibility": {
       "status": "ELIGIBLE"
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

`POST https://api.ads.apple.com/v1/business-brands/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Get Brand by ID](get-brand-by-id.md)
  Retrieve a single brand by its unique identifier.
- [Query Business Categories](query-categories.md)
  Retrieve a paginated list of business categories using filters and sorting.
- [Get Business Category](get-category-by-id.md)
  Retrieve a single business category by its identifier.
- [Query Rejection Reasons for Brands](query-policy-assignments-(rejection-reasons)-for-external-consumers.md)
  Query paginated policy assignment rejection reason details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-brands)*