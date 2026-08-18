# Get Me Details

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Return the user ID and organization ID of the authenticated API caller.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint returns the `userId` and `orgId` associated with the access token used to authenticate the request. To confirm which user account is active and retrieve the root organization for subsequent API calls, use this endpoint.

#### Payload Examples

##### Request

```None
GET https://api.ads.apple.com/v1/me
```

##### Response

```json
{
 "result": {
   "userId": 3962840,
   "orgId": 27154130
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/me`

## See Also

- [Get User ACL](get-user-acls.md)
  Return the ad accounts and roles accessible to the authenticated API caller.
- [Get Org by ID](get-orgs-_id_.md)
  Retrieve the details of a specific organization by its ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-current-user-details)*