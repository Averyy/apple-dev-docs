# Update Ad Accounts

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Update an ad account’s name or delegations.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

- This endpoint updates an ad account’s `name` or `delegations`. See [`AdAccountUpdate`](adaccountupdate.md) for field-level mutability details.
- The `delegations` field is optional and nullable.
- When included, each entry requires a `resourceType` and a `resourceId`.
- Like a promoted object, a delegation always identifies its resource by type and ID: `CONTENT_PROVIDER` takes a Content Provider ID (CPID), and `BUSINESS_BRAND` takes a Brand ID. See [`AdvertiserResourceType`](advertiserresourcetype.md) for all supported values.
- Providing the `delegations` array replaces all existing delegations in full: the update keeps the items you include and removes the items you omit.
- To link an App Store Connect account, include a `CONTENT_PROVIDER` delegation with the CPID as `resourceId`. See [`ProductFeatures`](productfeatures.md) for delegation requirements by App Store or Apple Maps.

#### Payload Examples

**Update with CPID Delegation**:

All fields in the request body are optional. `delegations` is also nullable, but `name`, if provided, must not be null. Providing the `delegations` array replaces all existing delegations in full.

##### Request

```json
PUT /v1/ad-accounts/123456789

{
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
   "delegations": [
     {
       "resourceId": "12345678",
       "resourceType": "CONTENT_PROVIDER",
       "resourceName": "AwayFinder"
     }
   ],
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-06-01T10:00:00.000"
 }
}
```

**Update with Brand ID Delegation**:

Renames the account and replaces the full set of delegations. All array fields use full-replacement semantics.

##### Request

```json
PUT /v1/ad-accounts/123456789

{
 "name": "AwayFinder Ad Account Updated",
 "delegations": [
   {
     "resourceId": "9151314442816847872",
     "resourceType": "BUSINESS_BRAND"
   }
 ]
}
```

##### Response

```json
{
 "result": {
   "id": 123456789,
   "name": "AwayFinder Ad Account Updated",
   "orgId": 987654321,
   "timezone": "America/New_York",
   "currency": "USD",
   "paymentModel": "PAYG",
   "systemStatus": "ACTIVE",
   "delegations": [
     {
       "resourceId": "9151314442816847872",
       "resourceType": "BUSINESS_BRAND",
       "resourceName": "AwayFinder"
     }
   ],
   "creationTime": "2025-01-10T08:00:00.000",
   "modificationTime": "2025-06-01T10:00:00.000"
 }
}
```

## Endpoint

`PUT https://api.ads.apple.com/v1/ad-accounts/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create Ad Accounts](post-ad-accounts.md)
  Create a new ad account under a specified organization.
- [Get Ad Account by ID](get-ad-accounts-_id_.md)
  Retrieve the full details of a specific ad account by its ID.
- [Get Advertiser Resources](get-advertiser-resources.md)
  Retrieve the advertiser resources available to your organization, filtered by resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/put-ad-accounts-_id_)*