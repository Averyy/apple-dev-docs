# Get Ad Account by ID

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieve the full details of a specific ad account by its ID.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

This endpoint retrieves the full details of a specific ad account by its ID, including its associated advertiser resources.

#### Payload Examples

##### Request

```
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

### Path Parameters

- `id` (string) *(required)*

### Header Parameters

- `X-Ap-Context` (string) *(required)*

## Responses

- `200` OK (`AdAccountResponse`, `application/json`): Successful operation. Returns [`AdAccountResponse`](./adaccountresponse.md) (`result`: [`AdAccount`](./adaccount.md)).
- `400` Bad Request (`ErrorResponse`, `application/json`): Bad Request. Returns [`ErrorResponse`](./errorresponse.md).
- `401` Unauthorized (`ErrorResponse`, `application/json`): Unauthorized.
- `403` Forbidden (`ErrorResponse`, `application/json`): Forbidden.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found. Returns [`ErrorResponse`](./errorresponse.md).
- `429` Too Many Requests (`ErrorResponse`, `application/json`): Rate Limit Exceeded. See [Applying Rate Limits](./rate-limits.md).
- `500` Internal Server Error (`ErrorResponse`, `application/json`): Internal Server Error. Returns [`ErrorResponse`](./errorresponse.md).

## See Also

- [Create Ad Accounts](./post-ad-accounts.md)
  Create a new ad account under a specified organization.
- [Update Ad Accounts](./put-ad-accounts-_id_.md)
  Update an ad account’s name or delegations.
- [Get Advertiser Resources](./get-advertiser-resources.md)
  Retrieve the advertiser resources available to your organization, filtered by resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-ad-accounts-_id_)*