# Get Advertiser Resources

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieve the advertiser resources available to your organization, filtered by resource type.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

Advertiser resources are brands and content providers available across your organization that you can delegate to an ad account. This endpoint returns all resources visible to the authenticated caller for the given `resourceType`. It takes no account-scoping parameter. The `resourceType` query parameter is required. Omitting it returns an error. See [`AdvertiserResourceType`](./advertiserresourcetype.md) for supported values.

Each resource in the response identifies itself by its `resourceId`, `resourceType`, and `resourceName`. Use the returned `resourceId` values when creating or updating delegations on an ad account via [`Update Ad Accounts`](./put-ad-accounts-_id_.md).

#### Payload Examples

##### Request

```
GET /v1/advertiser-resources?resourceType=CONTENT_PROVIDER
```

##### Response

```json
{
 "result": [
   {
     "resourceId": "987654321",
     "resourceType": "CONTENT_PROVIDER",
     "resourceName": "AwayFinder"
   }
 ]
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/advertiser-resources`

## Parameters

### Query Parameters

- `resourceType` (AdvertiserResourceType) *(required)*

## Responses

- `200` OK (`AdvertiserResourceListResponse`, `application/json`): Successful operation. Returns [`AdvertiserResourceListResponse`](./advertiserresourcelistresponse.md) (`result`: array of [`Delegation`](./delegation.md)).
- `400` Bad Request (`Error`, `application/json`): Bad Request. Returns [`ErrorResponse`](./errorresponse.md).
- `401` Unauthorized (`Error`, `application/json`): Unauthorized.
- `403` Forbidden (`Error`, `application/json`): Forbidden.
- `404` Not Found (`Error`, `application/json`): Resource not found. Returns [`ErrorResponse`](./errorresponse.md).
- `429` Too Many Requests (`Error`, `application/json`): Rate Limit Exceeded. See [Applying Rate Limits](./rate-limits.md).
- `500` Internal Server Error (`Error`, `application/json`): Internal Server Error. Returns [`ErrorResponse`](./errorresponse.md).

## See Also

- [Create Ad Accounts](./post-ad-accounts.md)
  Create a new ad account under a specified organization.
- [Get Ad Account by ID](./get-ad-accounts-_id_.md)
  Retrieve the full details of a specific ad account by its ID.
- [Update Ad Accounts](./put-ad-accounts-_id_.md)
  Update an ad account’s name or delegations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-advertiser-resources)*