# Get User ACL

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches roles and organizations that the API has access to.

**Availability**:
- Search Ads 5.0+

#### Discussion

The API uses a user access control list (ACL) for policy-based authorization to determine access to resources. The Get User ACL call fetches roles in all organizations. Each role has access to all organizations or a subset of them.

##### Get User Acl Example

**Request**:

```None
GET https://api.searchads.apple.com/api/v5/acls
```

**Response**:

```json
{
  "data": {
    "orgName": "Trip Trek",
    "orgId": 40669820,
    "currency": "USD",
    "timeZone": "America/Los_Angeles",
    "paymentModel": "PAYG",
    "roleNames": [
      "Admin"
    ],
    "parentOrgId": "27154130",
    "displayName": "Trip Trek"
  },
  "pagination": null,
  "error": null
}
```

##### Campaign Groups

The API treats your `orgId` like a campaign group. If you need to manage Apple Ads for multiple clients, or if you need to restrict user access to a subset of your campaigns, you can create additional campaign groups within your account. Otherwise, you can create and manage all your campaigns under your default `orgId` and campaign group.

## Endpoint

`GET https://api.searchads.apple.com/api/v5/acls`

## See Also

- [object UserAcl](useracl.md)
  The response to ACL requests.
- [object UserAclListResponse](useracllistresponse.md)
  A container for ACL call responses.
- [Get Me Details](get-me-details.md)
  Fetches details of an API caller.
- [object MeDetail](medetail.md)
  The API caller identifiers.
- [object MeDetailResponse](medetailresponse.md)
  The response from me detail calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-user-acl)*