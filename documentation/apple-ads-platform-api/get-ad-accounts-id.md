# Get Ad Account by ID

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve the full details of a specific ad account by its ID.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves the full details of a specific ad account by its ID, including its associated advertiser resources.

#### Payload Examples

##### Request

```None
GET https://api.ads.apple.com/v1/ad-accounts/123456789
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

## Endpoint

`GET https://api.ads.apple.com/v1/ad-accounts/{id}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Create Ad Accounts](post-ad-accounts.md)
  Create a new ad account under a specified organization.
- [Update Ad Accounts](put-ad-accounts-_id_.md)
  Update an ad account’s name or delegations.
- [Get Advertiser Resources](get-advertiser-resources.md)
  Retrieve the advertiser resources available to your organization, filtered by resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-ad-accounts-_id_)*