# Query Product Pages

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Queries App Store product pages available to your account.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

This endpoint queries product pages available to your ad account, returning Custom Product Pages (CPPs). Product pages come from App Store Connect and reflect the current publishing state of your product pages.

Filter by `adamId` to list all product pages for a specific app. This is the recommended starting point when building a `CUSTOM_PRODUCT_PAGE` creative: use this endpoint to discover the available `productPageId` values for an app, then fetch locale details or pass the ID directly to the creative creation endpoint.

Changes made in App Store Connect, such as publishing, hiding, or editing a product page, appear in this endpoint’s results after a short propagation delay.

See [`QueryFilterOperator`](./queryfilteroperator.md) for the full set of supported comparison operators.

##### Filterable Fields

| Field | Type | Operators | Sortable | Description |
| --- | --- | --- | --- | --- |
| `adamId` | integer | `EQUALS` |  | Filter to all product pages for a specific app. |
| `state` | string | `EQUALS` |  | Filter by page state: `VISIBLE` or `HIDDEN`. |

The request body is a [`QueryRequest`](./queryrequest.md) composed of [`QueryFilter`](./queryfilter.md) conditions and [`QuerySort`](./querysort.md) directives ([`QuerySortOrder`](./querysortorder.md)), controlled by [`QueryPagination`](./querypagination.md).

Keep the following constraints in mind when querying product pages:

| Constraint | Detail |
| --- | --- |
| X-AP-Context header | Required. Send `X-AP-Context: adAccountId=<id>`. Without it, the API returns `403 Forbidden`. |
| Filter by adamId | Always filter by `adamId` for targeted results. Omitting it may return product pages across all accessible apps. |
| App Store Connect source | Product page data originates in App Store Connect. This endpoint is read-only. |

#### Payload Examples

##### Request

```http
POST /v1/product-pages/query

{
 "filters": [
   {
     "field": "adamId",
     "operator": "EQUALS",
     "value": 123456789
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
     "id": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
     "adamId": 123456789,
     "name": "AwayFinder - Holiday Season CPP",
     "state": "VISIBLE",
     "deepLink": "awayfinder://campaign/holiday",
     "creationTime": "2025-04-10T08:00:00.000",
     "modificationTime": "2025-05-01T14:30:00.000"
   },
   {
     "id": "a4b2c3d4-e5f6-7890-abcd-ef1234567890",
     "adamId": 123456789,
     "name": "AwayFinder - Back to School CPP",
     "state": "VISIBLE",
     "deepLink": "",
     "creationTime": "2025-07-15T09:00:00.000",
     "modificationTime": "2025-07-20T11:00:00.000"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/product-pages/query`

## Parameters

### Header Parameters

- `X-AP-Context` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `QueryRequest`

## Responses

- `200` OK (`ProductPageDetailsQueryResponse`, `application/json`)
- `400` Bad Request (`ProductPageDetailsQueryResponse`, `application/json`)
- `401` Unauthorized (`Error`, `application/json`)
- `403` Forbidden (`Error`, `application/json`)
- `404` Not Found (`Error`, `application/json`)
- `429` Too Many Requests (`Error`, `application/json`)
- `500` Internal Server Error (`Error`, `application/json`)

## See Also

- [Get Product Page by ID](./get-product-page-by-id.md)
  Retrieves a specific Custom Product Page (CPP) by its unique UUID.
- [Query Product Page Locale Details](./query-product-page-locale-details.md)
  Queries the localized content of custom product pages (CPPs).
- [Query App Locale Details](./query-default-product-page-locale-details-by-adam-id.md)
  Returns the default product page locale details for an app identified by its adamId.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-product-pages)*