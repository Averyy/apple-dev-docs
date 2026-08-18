# Get Org by ID

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve the details of a specific organization by its ID.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves the details of a specific organization by its ID. To retrieve your organization ID, call [`Get Me Details`](get-current-user-details.md), which returns the `orgId` bound to the authenticated user.

#### Payload Examples

##### Request

```None
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

- `id` (string) *(required)*

## See Also

- [Get Me Details](get-current-user-details.md)
  Return the user ID and organization ID of the authenticated API caller.
- [Get User ACL](get-user-acls.md)
  Return the ad accounts and roles accessible to the authenticated API caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-orgs-_id_)*