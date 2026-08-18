# Get an Ad Creative

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Fetch a single ad creative by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves a single ad creative by its unique identifier. The response includes the full ad creative object, including type, spec, destination, current review state, and eligibility details.

The `systemStatus` field conveys the ad creative’s current operational state, reflecting the internal review outcome. To determine whether the ad creative is eligible to serve, check `systemStatus` (`VALID`, `INVALID`, `PENDING`) together with the `eligibility.status` field.

##### Understand System Status and Ad Delivery

While `systemStatus` is `PENDING`, any ads associated with this ad creative will also have `systemStatus: NOT_RUNNING` and will not deliver impressions. Once the ad creative reaches `VALID`, associated ads resume normal delivery, provided the ad group and campaign are also active.

The `eligibility` object in the response describes any policy or content restrictions that apply to the ad creative. This can include blocked countries, restricted placements, or content category limitations that affect where the ad creative is allowed to serve.

A couple of edge cases are worth calling out when fetching an ad creative by ID.

| Constraint | Detail |
| --- | --- |
| Deleted ad creatives | Fetching a deleted ad creative by ID returns a 404. Use the query endpoint with `"deleted": true` to retrieve deleted records. |
| Eligibility details | The system populates the `eligibility` object after review completes. It is empty or `null` while `systemStatus` is `PENDING`. |

#### Payload Examples

**Product Page Creative**:

##### Request

Retrieves a custom product page ad creative. The response includes the full ad creative object with its current review state and eligibility details.

```None
GET https://api.ads.apple.com/v1/creatives/666777888
```

##### Response

```json
{
 "result": {
   "id": 666777888,
   "adAccountId": 123456789,
   "name": "AwayFinder - Summer Campaign Creative",
   "creativeType": "CUSTOM_PRODUCT_PAGE",
   "creativeSpec": {},
   "destination": {
     "destinationType": "APP_STORE_PRODUCT_PAGE",
     "parameters": {
       "adamId": "987654321",
       "productPageId": "76659d7a-d146-43d3-b6b8-b7a12f74bf6b"
     },
     "url": "https://apps.apple.com/us/app/id/987654321"
   },
   "systemStatus": "VALID",
   "systemStatusReasons": [],
   "eligibility": {
     "status": "ELIGIBLE",
     "allowedGroups": [
       {
         "supplyPlacement": ["APPSTORE_SEARCH_RESULTS"],
         "countryOrRegion": ["US"]
       }
     ],
     "blockedGroups": []
   },
   "deleted": false,
   "creationTime": "2025-06-01T10:00:00.000",
   "modificationTime": "2025-06-01T10:00:00.000"
 }
}
```

**Apple Maps Creative**:

##### Request

Retrieves an Apple Maps ad creative. The response includes the ad creative spec with localized text and brand configuration.

```None
GET https://api.ads.apple.com/v1/creatives/666777889
```

##### Response

```json
{
 "result": {
   "id": 666777889,
   "adAccountId": 123456789,
   "name": "AwayFinder - Store Promotion Creative",
   "creativeType": "LOCAL_ADS_SEARCH_CREATIVE",
   "creativeSpec": {
     "localizedText": {
       "en-US": {
         "promoText": "Visit us today for special offers!"
       }
     },
     "brandId": "111222",
     "creativeAssets": [
       {
         "assetId": "770e8400-e29b-41d4-a716-446655440002"
       }
     ],
     "defaultLocale": "en-US"
   },
   "destination": {
     "destinationType": "LOCAL_ADS_PLACECARD"
   },
   "systemStatus": "VALID",
   "systemStatusReasons": [],
   "eligibility": {
     "status": "ELIGIBLE",
     "allowedGroups": [
       {
         "supplyPlacement": ["MAPS_SEARCH_RESULTS", "MAPS_SEARCH_HOME"]
       }
     ],
     "blockedGroups": []
   },
   "deleted": false,
   "creationTime": "2025-06-01T10:05:00.000",
   "modificationTime": "2025-06-01T10:05:00.000"
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/creatives/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad Creative](post-creatives.md)
  Add a new ad creative that defines the visual presentation and tap destination for an ad.
- [Query Ad Creatives](post-creatives-query.md)
  Retrieve ad creatives that match structured filter, sort, and pagination criteria.
- [Update an Ad Creative](put-creatives-_id_.md)
  Change an ad creative’s name or creative spec by its unique identifier.
- [Delete an Ad Creative](delete-creatives-_id_.md)
  Remove an ad creative by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-creatives-_id_)*