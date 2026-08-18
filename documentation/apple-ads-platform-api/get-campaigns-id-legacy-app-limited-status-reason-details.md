# Get Legacy App Limited Status Reason Details

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Return a map of country or region codes to their associated limited-status reason for legacy app campaigns.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

Use this endpoint to diagnose why specific campaigns are not delivering in one or more countries or regions. The response contains information on why delivery is limited in each market.

#### Payload Examples

Returns limited-status reasons per country or region for legacy app campaigns in the scoped ad account.

##### Request

No request body is required. Include the `X-Ap-Context` header with your `adAccountId`.

```None
GET https://api.ads.apple.com/v1/campaigns/{id}/legacy-app-limited-status-reason-details
```

##### Response

```json
{
 "result": {
   "countryOrRegionLimitedStatusReasons": {
     "US": [
       "APP_NOT_ELIGIBLE_SUPPLY_PLACEMENT",
       "APP_NOT_PUBLISHED_YET"
     ],
     "GB": [
       "APP_NOT_PUBLISHED_YET"
     ],
     "AU": []
   }
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/campaigns/{id}/legacy-app-limited-status-reason-details`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create a Campaign](post-campaigns.md)
  Create a new advertising campaign with a promoted object, budget, targeting, and bid strategy configuration.
- [Query Campaigns](post-campaigns-query.md)
  Query campaigns using filters, sorting, and pagination.
- [Get a Campaign](get-campaigns-_id_.md)
  Retrieve a single campaign by its unique identifier.
- [Update a Campaign](put-campaigns-_id_.md)
  Update a campaign’s name, status, budget, targeting, or bid strategy.
- [Delete a Campaign](delete-campaigns-_id_.md)
  Soft-delete a campaign by its unique identifier, cascading to its ad groups, keywords, and ads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-campaigns-_id_-legacy-app-limited-status-reason-details)*