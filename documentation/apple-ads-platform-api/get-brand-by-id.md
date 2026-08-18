# Get Brand by ID

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve a single brand by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves a single brand by its ID. The brand `id` in the response is the same value you use as `promotedObjectId` when creating a `BUSINESS_BRAND` campaign.

#### Payload Examples

##### Request

Retrieves the brand with the given ID and returns its country or region, categories, and current eligibility status.

```None
GET https://api.ads.apple.com/v1/business-brands/9151314442816847872
```

##### Response

```json
{
 "result": {
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
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/business-brands/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Brands](query-brands.md)
  Retrieve a paginated list of brands using filters and sorting.
- [Query Business Categories](query-categories.md)
  Retrieve a paginated list of business categories using filters and sorting.
- [Get Business Category](get-category-by-id.md)
  Retrieve a single business category by its identifier.
- [Query Rejection Reasons for Brands](query-policy-assignments-(rejection-reasons)-for-external-consumers.md)
  Query paginated policy assignment rejection reason details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-brand-by-id)*