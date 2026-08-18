# Query Rejection Reasons

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Query ad creative rejection reasons for apps and return why each ad creative failed approval.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves a list of ad creative rejection reasons based on filtering and pagination criteria. See [`CreativeRejectionReason`](creativerejectionreason.md) for the full field reference, including `creativeId` and the `reasonLevel` values.

#### Payload Examples

##### Request

```json
POST /v1/rejection-reasons/apps/query

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
   "pageSize": 20
 },
 "sorting": [
   {
     "field": "id",
     "order": "DESC"
   }
 ]
}
```

##### Response

```json
{
 "result": [
   {
     "id": 112233445,
     "adamId": 123456789,
     "creativeId": 456789,
     "productPageId": "1a2b3c4d-0001",
     "assetId": null,
     "supplySource": "APPSTORE",
     "supplyPlacement": "APPSTORE_SEARCH_RESULTS",
     "countryOrRegion": "US",
     "languageCode": "en-US",
     "reasonType": "REJECTION_REASON",
     "reasonCode": "APP_NOT_ELIGIBLE",
     "comment": null,
     "reasonLevel": "CUSTOM_PRODUCT_PAGE_LOCALE",
     "creationTime": "2026-02-05T08:30:00.000",
     "modificationTime": "2026-03-05T08:30:00.000"
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

`POST https://api.ads.apple.com/v1/rejection-reasons/apps/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [App Eligibility Endpoints](app-eligibility-endpoints.md)
  Check whether apps qualify to run ads and look up rejection reasons for creatives.
- [Check App Eligibility](find-apps-eligibilities.md)
  Check whether apps are eligible to run on certain Apple Ads placements and in specific countries or regions.
- [Get Rejection Reasons](gets-rejection-reasons-by-id.md)
  Retrieve the details of an ad creative rejection reason by ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/find-rejection-reasons)*