# AdAccountCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request body for creating a new ad account under an organization.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AdAccountCreate
```

#### Discussion

`AdAccountCreate` is the request body for `POST /v1/ad-accounts`.

##### Example

```json
{
  "name": "AwayFinder Ad Account",
  "productFeatures": [
    "APPSTORE_APP_MANUAL"
  ],
  "delegations": [
    {
      "resourceId": "12345678",
      "resourceType": "CONTENT_PROVIDER"
    }
  ]
}
```

## Properties

- `name` (string) *(required)*: The display name of the ad account.
- `delegations` ([DelegationCreate]): Advertiser resource delegations to associate with the ad account, matching the account’s `productFeatures` value. Use a `CONTENT_PROVIDER` delegation for App Store advertising, or a `BUSINESS_BRAND` delegation for Apple Maps advertising. See [`DelegationCreate`](delegationcreate.md).
- `productFeatures` ([ProductFeatures]) *(required)*: Product features enabled for this ad account. Set to `APPSTORE_APP_MANUAL` for App Store advertising or `BUSINESS_BRAND_MANUAL` for Apple Maps advertising. Each ad account is authorized for one or the other, not both. If your organization needs both, create a separate ad account for each. See [`ProductFeatures`](productfeatures.md) for how each feature affects campaign eligibility.

## See Also

- [object AdAccount](adaccount.md)
  The account-level resource within an organization that contains campaigns and advertising settings.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adaccountcreate)*