# User ACL

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

An access control entry for a single ad account that specifies the authenticated user’s assigned roles.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object UserAcl
```

#### Discussion

`UserAcl` represents a user’s access control entry for a single ad account. Each record returned by `GET /v1/acls` corresponds to one ad account the authenticated user can access.

##### Example

```json
{
  "adAccount": {
    "id": 123456789,
    "name": "AwayFinder",
    "orgId": 987654321
  },
  "roles": [
    "Admin"
  ]
}
```

#### Roles Reference

An API Account Manager assigns roles through the Apple Ads UI, and you can’t set or change them via the API. Use the table below as a reference when interpreting the `roles` field returned by `GET /v1/acls`.

| Role | Access Level |
| --- | --- |
| `Admin` | Full read and write access to the ad account |
| `API Account Manager` | Full read and write access |
| `API Account Read Only` | Read-only access to all resources |
| `Limited Access: API Read & Write` | Read/write access to a limited resource set |
| `Limited Access: API Read Only` | Read-only access to a limited resource set |

## Properties

- `adAccount` (AclAdAccount): The ad account this ACL entry belongs to. See [`AclAdAccount`](acladaccount.md).
- `roles` ([string]): List of role names the user holds for this ad account.

## See Also

- [object AdAccount](adaccount.md)
  The account-level resource within an organization that contains campaigns and advertising settings.
- [object AdAccountCreate](adaccountcreate.md)
  Request body for creating a new ad account under an organization.
- [object AdAccountUpdate](adaccountupdate.md)
  The request body you use to update an ad account.
- [object AdAccountResponse](adaccountresponse.md)
  The response envelope ad account operations return.
- [object AclAdAccount](acladaccount.md)
  Ad account details as returned in ACL responses.
- [object UserAclListResponse](useracllistresponse.md)
  The response envelope for the Get User ACL endpoint, containing the list of user access control entries.
- [object UserAccessResult](useraccessresult.md)
  The result object returned when querying user ACL entries, containing the list of ad account access records.
- [object Delegation](delegation.md)
  Links an ad account to an external advertiser resource, such as a content provider or brand.
- [object DelegationCreate](delegationcreate.md)
  The request body for creating a delegation on an ad account.
- [object DelegationUpdate](delegationupdate.md)
  The request body for updating a delegation on an ad account.
- [object Me](me.md)
  The authenticated user’s identity information.
- [object MeResponse](meresponse.md)
  The response envelope for the Get Me Details endpoint, containing the authenticated user’s identity.
- [object Org](org.md)
  Represents an organization in the Apple Ads system.
- [object OrgResponse](orgresponse.md)
  The response envelope for a single organization lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/useracl)*