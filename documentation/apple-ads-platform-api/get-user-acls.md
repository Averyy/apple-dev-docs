# Get User ACL

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Return the ad accounts and roles accessible to the authenticated API caller.

**Availability**:
- Apple Ads Platform API 1.0+

#### Discussion

This endpoint retrieves a `UserAclListResponse` for the authenticated user. The response contains a `result` object with an `acls` array. Each `UserAcl` entry contains an `adAccount` object and a `roles` array listing the roles the user holds for that account.

To discover which ad accounts an API token can access and what permission level applies, use this endpoint at the start of a session. Each access token binds to exactly one org. The `orgId` on every returned `adAccount` will be the same.

#### Payload Examples

##### Request

```None
GET https://api.ads.apple.com/v1/acls
```

##### Response

```json
{
 "result": {
   "acls": [
     {
       "adAccount": {
         "id": 123456789,
         "name": "AwayFinder",
         "orgId": 40669820
       },
       "roles": [
         "Admin"
       ]
     }
   ]
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/acls`

## See Also

- [Get Me Details](get-current-user-details.md)
  Return the user ID and organization ID of the authenticated API caller.
- [Get Org by ID](get-orgs-_id_.md)
  Retrieve the details of a specific organization by its ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-user-acls)*