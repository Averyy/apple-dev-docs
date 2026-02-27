# UserAcl

**Framework**: Apple Ads  
**Kind**: dictionary

The response to ACL requests.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object UserAcl
```

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

## Properties

- `currency` (string): The organization’s default currency that is set up in [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com/).
- `orgId` (int64): The identifier of the organization that owns the campaign. Your `orgId` is the same as your account in [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com/).
- `orgName` (string): The name of your organization.
- `parentOrgId` (int64): Distinguishes the account from an `orgId` belonging to a suborganization.
- `paymentModel` (string): The payment model that you set through [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com/). If you don’t set a payment model, campaigns can’t run. - **`PAYG`**: A pay-as-you-go payment model.
- **`LOC`**: A line-of-credit payment model.
- **`<empty string>`**: There is no set payment method. If you don’t select a payment model, you can still create campaigns. You must select a payment model before a campaign is eligible to run. See [`Budget Orders`](budget-orders.md) for endpoints used to manage budget orders.
- `roleNames` ([string]): Each role governs what a user can see and do within the account: - **API Account Manager**: Manage all campaigns within an account with read-and-write capabilities. View reporting across the organization. Create and edit an API public key. - **API Account Read Only**: View reporting across the account with read-only permission. Create and edit an API public key. - **Limited Access**: API Read & Write: View reporting. Manage all campaigns and settings within a campaign group with read-and-write capabilities. Create and edit an API public key.
- **Limited Access**: API Read Only: View reporting across the organization. Create and edit an API public key.
- `timeZone` (string): The time zone you set during account creation through [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com). `ORTZ`, the organization time zone, is the default.

## See Also

- [Get User ACL](get-user-acl.md)
  Fetches roles and organizations that the API has access to.
- [object UserAclListResponse](useracllistresponse.md)
  A container for ACL call responses.
- [Get Me Details](get-me-details.md)
  Fetches details of an API caller.
- [object MeDetail](medetail.md)
  The API caller identifiers.
- [object MeDetailResponse](medetailresponse.md)
  The response from me detail calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/useracl)*