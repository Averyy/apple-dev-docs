# Query Business Categories

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a paginated list of business categories using filters and sorting.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns a paginated list of business categories from the Maps taxonomy. Categories classify brands and locations. You use them to scope targeting and discovery within Apple Maps campaigns. An empty request body returns all categories with default pagination.

Each category has a `qualifiedId` using a dot to separate each level of the taxonomy hierarchy (for example, `dining.restaurant`). A single hierarchy level’s own name can itself contain underscores (for example, `association_or_organization`), so a dot always marks a hierarchy boundary, but an underscore does not. Use the `text` value on a `CATEGORY` match-type [`Keyword`](keyword.md) to target Apple Maps searches within that category.

#### Request Body

See [`QueryRequest`](queryrequest.md).

Each category record returned includes the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Unique category identifier (MUID). |
| `name` | string | English display name of the category. |
| `qualifiedId` | string | Dot-delimited taxonomy path. Example: `dining.restaurant`. |
| `eligibility` | object | Ad serving eligibility for this category. See [`Eligibility`](eligibility.md). |
| `creationTime` | string | ISO-8601 creation timestamp. Read-only. |
| `modificationTime` | string | ISO-8601 last-modified timestamp. Read-only. |

The `qualifiedId` format and eligibility status both carry specific rules:

| Constraint | Detail |
| --- | --- |
| `qualifiedId` format | Dot-delimited hierarchy string. A dot always marks a hierarchy boundary, but an individual level’s name can itself contain underscores. Use this value as the `text` on a `CATEGORY` match-type Keyword. |
| Eligibility check | Only categories with `ELIGIBLE` status can be used in active Apple Maps campaigns. |

#### Payload Examples

**Query All Categories**:

Retrieve all business categories with default pagination.

##### Request

```json
{}
```

##### Response

```json
{
 "result": [
   {
     "id": "cat-din-001",
     "name": "Restaurant",
     "qualifiedId": "dining.restaurant",
     "creationTime": "2024-06-01T00:00:00Z",
     "modificationTime": "2024-06-01T00:00:00Z",
     "eligibility": {
       "status": "ELIGIBLE",
       "blockedGroups": [],
       "allowedGroups": []
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

**Filter by Name**:

Find categories with a specific name prefix.

##### Request

```json
{
 "filters": [
   {
     "field": "name",
     "operator": "STARTS_WITH",
     "value": "Dining"
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
     "id": "cat-din-001",
     "name": "Dining",
     "qualifiedId": "dining",
     "eligibility": {
       "status": "ELIGIBLE"
     }
   },
   {
     "id": "cat-din-002",
     "name": "Dining - Restaurant",
     "qualifiedId": "dining.restaurant",
     "eligibility": {
       "status": "ELIGIBLE"
     }
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

`POST https://api.ads.apple.com/v1/business-categories/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Brands](query-brands.md)
  Retrieve a paginated list of brands using filters and sorting.
- [Get Brand by ID](get-brand-by-id.md)
  Retrieve a single brand by its unique identifier.
- [Get Business Category](get-category-by-id.md)
  Retrieve a single business category by its identifier.
- [Query Rejection Reasons for Brands](query-policy-assignments-(rejection-reasons)-for-external-consumers.md)
  Query paginated policy assignment rejection reason details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-categories)*