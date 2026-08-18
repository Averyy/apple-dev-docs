# Check App Eligibility

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Check whether apps are eligible to run on certain Apple Ads placements and in specific countries or regions.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint checks whether one or more apps are eligible to run Apple Ads campaigns in specified countries or regions. The response contains per-app eligibility status, along with the specific supply placements and markets where advertising is allowed or blocked.

To confirm that your app can be promoted in the target markets, use this endpoint before creating campaigns. Attempting to run campaigns in ineligible markets will result in zero delivery. Calling this endpoint early in the campaign setup workflow avoids wasted configuration.

Ineligibility reasons can include: the app is not available in that market, regional distribution restrictions set in App Store Connect, or Apple Ads policy violations.

#### Request Body

The `state` field resolves to one of the following values:

| Status | Description |
| --- | --- |
| `ELIGIBLE` | The app is approved to run ads in the specified country or region. |
| `INELIGIBLE` | The app cannot run ads in the specified country or region. |

##### Response Structure

Each item in `result` is a flat `EligibilityResponse` row for a specific combination of app, supply placement, supply source, country, and device class.

| Field | Type | Description |
| --- | --- | --- |
| `adamId` | integer (int64) | The Adam ID of the app. |
| `supplyPlacement` | string | The supply placement being checked. |
| `supplySource` | string | The supply source being checked. |
| `minAge` | number | The minimum age rating required to serve ads for this app in this market. |
| `state` | string | Eligibility state: `ELIGIBLE` or `INELIGIBLE` (default `ELIGIBLE`). |
| `countryOrRegion` | string | The country or region evaluated. |
| `deviceClass` | string | The device class evaluated. |
| `reasons` | array of strings | Codes explaining an `INELIGIBLE` state. |
| `creationTime` | string (ISO 8601) | When this eligibility record was created. |
| `modificationTime` | string (ISO 8601) | When this eligibility record was last modified. |

An app that is eligible in some placements and ineligible in others appears as multiple rows, one per combination.

Keep the following constraints in mind when checking eligibility:

| Constraint | Detail |
| --- | --- |
| Batch queries | Filter by multiple `adamId` values in a single request to check several apps at once. |
| Pre-campaign check | Always call this endpoint before creating campaigns in new markets. |
| Distribution restrictions | Ineligibility may reflect App Store Connect distribution settings, not just policy violations. |

#### Payload Examples

**Check Single App**:

##### Request

```json
POST /v1/eligibilities/apps/query

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
 }
}
```

##### Response

```json
{
 "result": [
   {
     "adamId": 123456789,
     "supplyPlacement": "APPSTORE_SEARCH_RESULTS",
     "supplySource": "APPSTORE",
     "minAge": 4,
     "state": "ELIGIBLE",
     "countryOrRegion": "US",
     "deviceClass": "IPHONE"
   },
   {
     "adamId": 123456789,
     "supplyPlacement": "APPSTORE_SEARCH_RESULTS",
     "supplySource": "APPSTORE",
     "minAge": 4,
     "state": "ELIGIBLE",
     "countryOrRegion": "GB",
     "deviceClass": "IPHONE"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

**Check Multiple Apps**:

##### Request

```json
POST /v1/eligibilities/apps/query

{
 "filters": [
   {
     "field": "adamId",
     "operator": "IN",
     "value": [
       123456789,
       987654321
     ]
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 50
 }
}
```

##### Response

```json
{
 "result": [
   {
     "adamId": 123456789,
     "supplyPlacement": "APPSTORE_SEARCH_RESULTS",
     "supplySource": "APPSTORE",
     "minAge": 4,
     "state": "ELIGIBLE",
     "countryOrRegion": "US",
     "deviceClass": "IPHONE"
   },
   {
     "adamId": 987654321,
     "supplyPlacement": "APPSTORE_SEARCH_RESULTS",
     "supplySource": "APPSTORE",
     "minAge": 4,
     "state": "ELIGIBLE",
     "countryOrRegion": "US",
     "deviceClass": "IPHONE"
   },
   {
     "adamId": 987654321,
     "supplyPlacement": "APPSTORE_SEARCH_RESULTS",
     "supplySource": "APPSTORE",
     "minAge": 17,
     "state": "INELIGIBLE",
     "countryOrRegion": "JP",
     "deviceClass": "IPHONE",
     "reasons": [
       "APP_NOT_ELIGIBLE_IN_STOREFRONT"
     ]
   }
 ],
 "pagination": {
   "totalCount": 3,
   "offset": 0,
   "pageSize": 50
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/eligibilities/apps/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## Request Body

See [`EligibilityQueryRequest`](eligibilityqueryrequest.md).

## See Also

- [Query Rejection Reasons](find-rejection-reasons.md)
  Query ad creative rejection reasons for apps and return why each ad creative failed approval.
- [Get Rejection Reasons](gets-rejection-reasons-by-id.md)
  Retrieve the details of an ad creative rejection reason by ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/find-apps-eligibilities)*