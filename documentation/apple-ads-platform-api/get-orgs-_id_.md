# Get Org by ID

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieve the details of a specific organization by its ID.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

This endpoint retrieves the details of a specific organization by its ID. To retrieve your organization ID, call [`Get Me Details`](./get-current-user-details.md), which returns the `orgId` bound to the authenticated user.

#### Payload Examples

##### Request

```
GET https://api.ads.apple.com/v1/orgs/987654321
```

##### Response

```json
{
 "result": {
   "id": 987654321,
   "name": "AwayFinder",
   "currency": "USD",
   "timezone": "America/New_York",
   "paymentModel": "PAYG",
   "systemStatus": "ACTIVE",
   "systemStatusReasons": []
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/orgs/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`OrgResponse`, `application/json`): Successful operation. Returns [`OrgResponse`](./orgresponse.md) (`result`: [`Org`](./org.md)).
- `400` Bad Request (`ErrorResponse`, `application/json`): Bad Request. Returns [`ErrorResponse`](./errorresponse.md).
- `401` Unauthorized (`ErrorResponse`, `application/json`): Unauthorized.
- `403` Forbidden (`ErrorResponse`, `application/json`): Forbidden.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found. Returns [`ErrorResponse`](./errorresponse.md).
- `429` Too Many Requests (`ErrorResponse`, `application/json`): Rate Limit Exceeded. See [Applying Rate Limits](./rate-limits.md).
- `500` Internal Server Error (`ErrorResponse`, `application/json`): Internal Server Error. Returns [`ErrorResponse`](./errorresponse.md).

## See Also

- [Get Me Details](./get-current-user-details.md)
  Return the user ID and organization ID of the authenticated API caller.
- [Get User ACL](./get-user-acls.md)
  Return the ad accounts and roles accessible to the authenticated API caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-orgs-_id_)*