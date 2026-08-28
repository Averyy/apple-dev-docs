# Query Ad Creatives

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve ad creatives that match structured filter, sort, and pagination criteria.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint queries ad creatives using the standard `QueryRequest` structure. The endpoint supports field filtering, multi-field sorting, and offset-based pagination. The system automatically scopes results to the ad accounts accessible to the authenticated caller. You can’t query by `adAccountId`. See [`Creatives Endpoints`](creatives-endpoints.md) for the fields you can filter on.

By default, results exclude deleted ad creatives. To include deleted records, add an explicit filter on `"field": "deleted", "operator": "EQUALS", "value": true`.

See [`QueryFilterOperator`](queryfilteroperator.md) for the full set of supported comparison operators.

##### Filterable Fields

| Field | Type | Operators | Sortable | Description |
| --- | --- | --- | --- | --- |
| `id` | integer | `EQUALS`, `IN` | Yes (default) | Primary identifier of the ad creative. |
| `adAccountId` | integer | `EQUALS` |  | Reference to the ad account. |
| `name` | string | `EQUALS`, `STARTS_WITH` |  | Name of the ad creative. |
| `creativeType` | string (enum) | `EQUALS`, `IN` |  | Type of ad creative. See [`CreativeType`](creativetype.md). |
| `systemStatus` | string (enum) | `EQUALS`, `IN` |  | System validation status. |
| `deleted` | boolean | `EQUALS` |  | Whether the ad creative has been deleted. Excluded by default unless explicitly filtered to `true`. |

The request body is a [`QueryRequest`](queryrequest.md) composed of [`QueryFilter`](queryfilter.md) conditions and [`QuerySort`](querysort.md) directives ([`QuerySortOrder`](querysortorder.md)), controlled by [`QueryPagination`](querypagination.md).

#### Payload Examples

**Query by Creative Type**:

##### Request

```json
{
 "filters": [
   {
     "field": "creativeType",
     "operator": "EQUALS",
     "value": "CUSTOM_PRODUCT_PAGE"
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": 666777888,
     "adAccountId": 123456789,
     "name": "AwayFinder - Summer Campaign Creative",
     "creativeType": "CUSTOM_PRODUCT_PAGE",
     "systemStatus": "VALID",
     "deleted": false,
     "creationTime": "2025-06-01T10:00:00.000",
     "modificationTime": "2025-06-01T10:00:00.000"
   }
 ]
}
```

**Query Invalid Creatives**:

##### Request

```json
{
 "filters": [
   {
     "field": "systemStatus",
     "operator": "EQUALS",
     "value": "INVALID"
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "id": 666777890,
     "adAccountId": 123456789,
     "name": "AwayFinder - Rejected Banner Creative",
     "creativeType": "LOCAL_ADS_SEARCH_CREATIVE",
     "systemStatus": "INVALID",
     "systemStatusReasons": [
       "POLICY_PROHIBITED"
     ],
     "deleted": false,
     "creationTime": "2025-05-15T08:00:00.000",
     "modificationTime": "2025-05-16T14:22:00.000"
   }
 ]
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/creatives/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad Creative](post-creatives.md)
  Add a new ad creative that defines the visual presentation and tap destination for an ad.
- [Get an Ad Creative](get-creatives-_id_.md)
  Fetch a single ad creative by its unique identifier.
- [Update an Ad Creative](put-creatives-_id_.md)
  Change an ad creative’s name or creative spec by its unique identifier.
- [Delete an Ad Creative](delete-creatives-_id_.md)
  Remove an ad creative by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-creatives-query)*