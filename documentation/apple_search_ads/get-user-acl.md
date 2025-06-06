# Get User ACL

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches roles and organizations that the API has access to.

**Availability**:
- Search Ads 5.0+

#### Discussion

The API uses a user access control list (ACL) for policy-based authorization to determine access to resources. The Get User ACL call fetches roles in all organizations. Each role has access to all organizations or a subset of them.

##### Get User Acl Example

##### Campaign Groups

The API treats your `orgId` like a campaign group. If you need to manage Search Ads for multiple clients, or if you need to restrict user access to a subset of your campaigns, you can create additional campaign groups within your account. Otherwise, you can create and manage all your campaigns under your default `orgId` and campaign group.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/get-user-acl)*