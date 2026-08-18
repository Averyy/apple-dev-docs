# Account Management Data Objects

**Framework**: Apple Ads Platform API

Reference the data objects for account management, access control, and organization resources.

**Availability**:
- Apple Ads Platform API 1.0+

## Topics

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
- [object UserAcl](useracl.md)
  An access control entry for a single ad account that specifies the authenticated user’s assigned roles.
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

## See Also

- [Managing Ad Accounts and API Access](access-overview.md)
  Authenticate your requests, scope them to an ad account, and apply role-based access levels.
- [Org & Me Endpoints](org-me.md)
  Retrieve the authenticated user’s identity, organization details, and ad account access list.
- [Ad Account Endpoints](ad-account-endpoints.md)
  Create, retrieve, and update ad accounts, and discover delegable advertiser resources.
- [Account Management Data Types](account-management-data-types.md)
  Reference the enumerations and scalar types for account management, access control, and organization resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/account-management-data-objects)*