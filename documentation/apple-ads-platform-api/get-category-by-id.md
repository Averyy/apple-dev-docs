# Get Business Category

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a single business category by its identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns the full `BusinessCategory` object for the specified category ID. Use this endpoint to look up the `qualifiedId`, display name, and eligibility status for a specific category. The `id` is the MUID, which you can obtain from the Query Business Categories endpoint.

#### Payload Examples

##### Request

```None
GET https://api.ads.apple.com/v1/business-categories/cat-din-001
```

##### Response

```json
{
 "result": {
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
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/business-categories/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Brands](query-brands.md)
  Retrieve a paginated list of brands using filters and sorting.
- [Get Brand by ID](get-brand-by-id.md)
  Retrieve a single brand by its unique identifier.
- [Query Business Categories](query-categories.md)
  Retrieve a paginated list of business categories using filters and sorting.
- [Query Rejection Reasons for Brands](query-policy-assignments-(rejection-reasons)-for-external-consumers.md)
  Query paginated policy assignment rejection reason details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-category-by-id)*