# Query Brands

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieve a paginated list of brands using filters and sorting.

**Availability**:
- Apple Ads Platform API 1.0+

## Discussion

This endpoint returns a paginated list of brands accessible to the ad account. An empty request body returns all brands with default pagination.

The brand `id` returned in results corresponds to the `promotedObjectId` used when creating `BUSINESS_BRAND` campaigns.

See [`QueryFilterOperator`](./queryfilteroperator.md) for the full set of supported comparison operators.

### Filterable Fields

| Field | Type | Operators | Sortable | Description |
| --- | --- | --- | --- | --- |
| `id` | string | `EQUALS`, `IN` |  | ID of the brand. |
| `eligibility.status` | string (enum) | `EQUALS` |  | Ad serving eligibility for the brand. See [`Eligibility`](./eligibility.md). |

The request body is a [`QueryRequest`](./queryrequest.md) composed of [`QueryFilter`](./queryfilter.md) conditions and [`QuerySort`](./querysort.md) directives ([`QuerySortOrder`](./querysortorder.md)), controlled by [`QueryPagination`](./querypagination.md).

## Request Body

See [`QueryRequest`](./queryrequest.md).

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `filters` | array | No | Filter conditions to narrow results. |
| `sorting` | array | No | Sort order for results (field + ASC/DESC). |
| `pagination` | object | No | Offset and page size. Defaults apply if omitted. |

## Payload Examples

**Query Brands**:

### Request

```http
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

### Response

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

### Request

Returns only brands you can use in a campaign. Confirm a brand’s eligibility with this filter before creating a Brands campaign, as described in [Ads on Apple Maps Endpoints](./brands-endpoints.md).

```http
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

### Response

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

### Header Parameters

- `X-AP-Context` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `QueryRequest`

## Responses

- `200` OK (`BrandQueryResponse`, `application/json`)
- `400` Bad Request (`BrandQueryResponse`, `application/json`)
- `401` Unauthorized (`Error`, `application/json`)
- `403` Forbidden (`Error`, `application/json`)
- `404` Not Found (`Error`, `application/json`)
- `429` Too Many Requests (`Error`, `application/json`)
- `500` Internal Server Error (`Error`, `application/json`)

## See Also

- [Get Brand by ID](./get-brand-by-id.md)
  Retrieve a single brand by its unique identifier.
- [Query Business Categories](./query-categories.md)
  Retrieve a paginated list of business categories using filters and sorting.
- [Get Business Category](./get-category-by-id.md)
  Retrieve a single business category by its identifier.
- [Query Rejection Reasons for Brands](./query-policy-assignments-%28rejection-reasons%29-for-external-consumers.md)
  Query paginated policy assignment rejection reason details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-brands)*