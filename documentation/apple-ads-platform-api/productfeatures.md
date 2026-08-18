# ProductFeatures

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Product features are the advertising capabilities for an ad account.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string ProductFeatures
```

#### Discussion

The `productFeatures` array on an [`AdAccount`](adaccount.md) controls whether campaigns in that account run on App Store or Apple Maps. You set `productFeatures` when creating an ad account (it’s required on `AdAccountCreate`). It can’t be changed after the account is created. An account is authorized for App Store or Apple Maps, not both.

An account configured for App Store advertising cannot create Apple Maps campaigns. An account configured for Apple Maps advertising cannot create App Store campaigns. If your organization needs campaigns on both App Store and Apple Maps, create a dedicated ad account for each.

##### Enable App Store Advertising

The `APPSTORE_APP_MANUAL` feature authorizes an ad account for App Store advertising. Campaigns in this account promote iOS apps across App Store placements. Every campaign must set `promotedObjectType` to `APPSTORE_APP` and identify the app by its `adamId`. The app must pass an eligibility check (see [`Check App Eligibility`](find-apps-eligibilities.md)) before the campaign can serve.

##### Enable Apple Maps Advertising

The `BUSINESS_BRAND_MANUAL` feature authorizes an ad account for Apple Maps advertising. Campaigns in this account promote brands on Apple Maps. Every campaign must set `promotedObjectType` to `BUSINESS_BRAND`.

##### Link the Required Delegations

Delegations link the appropriate advertiser resource to an ad account. For App Store accounts this will be a `CONTENT_PROVIDER`. For Apple Maps accounts this will be a `BUSINESS_BRAND`. This delegation, together with the matching `productFeatures` value, must be in place before campaigns can go live.

To promote an app with Apple Ads, you must link to an App Store Connect account. If you have multiple App Store Connect accounts, you can link each one to your Apple Ads account to promote the associated apps.

To link a resource, use [`Create Ad Accounts`](post-ad-accounts.md) (`POST /v1/ad-accounts`) or [`Update Ad Accounts`](put-ad-accounts-_id_.md) (`PUT /v1/ad-accounts/{id}`) with the `delegations` field. Set `resourceType` to one of the values defined in [`AdvertiserResourceType`](advertiserresourcetype.md). The `resourceId` is the CPID or Brand ID value.

**App Store: `CONTENT_PROVIDER`**

```json
{
  "resourceId": "12345678",
  "resourceType": "CONTENT_PROVIDER"
}
```

**Apple Maps: `BUSINESS_BRAND`**

```json
{
  "resourceId": "9876543",
  "resourceType": "BUSINESS_BRAND"
}
```

**Create: `POST /v1/ad-accounts`**

`delegations` is optional but when included, each entry requires `resourceId` and `resourceType`.

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

**Update: `PUT /v1/ad-accounts/{id}`**

`delegations` is optional and nullable. Providing the array replaces all existing delegations in full. This endpoint does not change `productFeatures`, which is fixed at creation.

```json
{
  "delegations": [
    {
      "resourceId": "12345678",
      "resourceType": "CONTENT_PROVIDER"
    }
  ]
}
```

See [`DelegationCreate`](delegationcreate.md) and [`DelegationUpdate`](delegationupdate.md) for full field details.

## See Also

- [type OrgSystemStatus](orgsystemstatus.md)
  System-derived operational status of an organization.
- [type OrgSystemStatusReason](orgsystemstatusreason.md)
  Reasons that can cause an organization’s system status to be `INACTIVE`.
- [type AdAccountSystemStatus](adaccountsystemstatus.md)
  System-derived operational status of an ad account.
- [type AdAccountSystemStatusReason](adaccountsystemstatusreason.md)
  Enumeration of reasons that can cause an ad account’s system status to be `INACTIVE`.
- [object AdvertiserResourceListResponse](advertiserresourcelistresponse.md)
  Response envelope for advertiser resource list requests.
- [type AdvertiserResourceType](advertiserresourcetype.md)
  The type of advertiser resource you delegate to an ad account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/productfeatures)*