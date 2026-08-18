# Update an Ad Creative

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Change an ad creative’s name or creative spec by its unique identifier.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

For this endpoint, only two fields are mutable after you create an ad creative: `name` and `creativeSpec`. The `creativeType` and `destination` are permanently fixed at creation time and cannot be changed. Not every field within `creativeSpec` is mutable. Refer to the specific creative type documentation for which sub-fields can be updated.

#### Payload Examples

**Update Name**:

##### Request

```json
{
 "name": "AwayFinder - Summer Campaign Creative - Revised"
}
```

##### Response

```json
{
 "result": {
   "id": 666777888,
   "adAccountId": 123456789,
   "name": "AwayFinder - Summer Campaign Creative - Revised",
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
   "deleted": false,
   "creationTime": "2025-06-01T10:00:00.000",
   "modificationTime": "2025-06-15T09:30:00.000"
 }
}
```

**Update Creative Spec**:

##### Request

```json
{
 "creativeSpec": {
   "localizedText": {
     "en-US": {
       "promoText": "New summer deals - shop now!"
     },
     "fr-FR": {
       "promoText": "Nouvelles offres d'été - achetez maintenant!"
     }
   },
   "brandId": "111222",
   "creativeAssets": [
     {
       "assetId": "770e8400-e29b-41d4-a716-446655440002"
     }
   ],
   "defaultLocale": "en-US"
 }
}
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
         "promoText": "New summer deals - shop now!"
       },
       "fr-FR": {
         "promoText": "Nouvelles offres d'été - achetez maintenant!"
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
   "systemStatus": "PENDING",
   "systemStatusReasons": [],
   "deleted": false,
   "creationTime": "2025-06-01T10:05:00.000",
   "modificationTime": "2025-06-15T11:00:00.000"
 }
}
```

## Endpoint

`PUT https://api.ads.apple.com/v1/creatives/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create an Ad Creative](post-creatives.md)
  Add a new ad creative that defines the visual presentation and tap destination for an ad.
- [Query Ad Creatives](post-creatives-query.md)
  Retrieve ad creatives that match structured filter, sort, and pagination criteria.
- [Get an Ad Creative](get-creatives-_id_.md)
  Fetch a single ad creative by its unique identifier.
- [Delete an Ad Creative](delete-creatives-_id_.md)
  Remove an ad creative by its unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/put-creatives-_id_)*