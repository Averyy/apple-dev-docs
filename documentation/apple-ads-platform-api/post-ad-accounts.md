# Create Ad Accounts

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Create a new ad account under a specified organization.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint creates a new ad account under a specified organization.

- The ad account inherits `currency`, `timezone`, and `paymentModel` from the parent org at creation time. These values are immutable after creation, as is the `orgId` relationship.
- `name` and `productFeatures` are both required. The system rejects the request if either is omitted.
- The `X-AP-Context` header is not required for this endpoint.
- To enable App Store advertising, include a `CONTENT_PROVIDER` delegation with the CPID as `resourceId`.
- To enable Maps advertising, include a `BUSINESS_BRAND` delegation with the Brand ID as `resourceId`.
- See [`ProductFeatures`](productfeatures.md) for delegation requirements by App Store or Apple Maps.

#### Payload Examples

**Request with CPID Delegation**:

Links the ad account to an App Store Connect account via a Content Provider ID (CPID). `delegations` is optional but when included, each entry requires `resourceId` and `resourceType`.

##### Request

```json
POST /v1/ad-accounts

{
 "name": "AwayFinder Ad Account",
 "productFeatures": [
   "APPSTORE_APP_MANUAL"
 ],
 "delegations": [
   {
     "resourceId": "12345678",
     "resourceType": "CONTENT_PROVIDER"
   }
 ]
}
```

##### Response

```json
{
 "result": {
   "id": 123456789,
   "name": "AwayFinder Ad Account",
   "orgId": 987654321,
   "timezone": "America/New_York",
   "currency": "USD",
   "paymentModel": "PAYG",
   "systemStatus": "ACTIVE",
   "systemStatusReasons": [],
   "productFeatures": [
     "APPSTORE_APP_MANUAL"
   ],
   "delegations": [
     {
       "resourceId": "12345678",
       "resourceType": "CONTENT_PROVIDER",
       "resourceName": "AwayFinder Apps"
     }
   ],
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

**Request with Maps Delegation**:

Links the ad account to a validated brand for Apple Maps advertising via a Brand ID. `productFeatures` must include `BUSINESS_BRAND_MANUAL` and the matching delegation must use `resourceType: BUSINESS_BRAND`.

##### Request

```json
POST /v1/ad-accounts

{
 "name": "AwayFinder Brand Ad Account",
 "productFeatures": [
   "BUSINESS_BRAND_MANUAL"
 ],
 "delegations": [
   {
     "resourceId": "9876543",
     "resourceType": "BUSINESS_BRAND"
   }
 ]
}
```

##### Response

```json
{
 "result": {
   "id": 123456790,
   "name": "AwayFinder Brand Ad Account",
   "orgId": 987654321,
   "timezone": "America/New_York",
   "currency": "USD",
   "paymentModel": "PAYG",
   "systemStatus": "ACTIVE",
   "systemStatusReasons": [],
   "productFeatures": [
     "BUSINESS_BRAND_MANUAL"
   ],
   "delegations": [
     {
       "resourceId": "9876543",
       "resourceType": "BUSINESS_BRAND",
       "resourceName": "AwayFinder"
     }
   ],
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-01-10T08:00:00.000"
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/ad-accounts`

## Parameters

- `X-Ap-Context` (string)

## See Also

- [Get Ad Account by ID](get-ad-accounts-_id_.md)
  Retrieve the full details of a specific ad account by its ID.
- [Update Ad Accounts](put-ad-accounts-_id_.md)
  Update an ad account’s name or delegations.
- [Get Advertiser Resources](get-advertiser-resources.md)
  Retrieve the advertiser resources available to your organization, filtered by resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/post-ad-accounts)*