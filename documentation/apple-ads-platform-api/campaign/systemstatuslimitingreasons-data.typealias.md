# Campaign.SystemStatusLimitingReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

A reason code indicating that a campaign is running but delivering at reduced capacity.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Campaign.SystemStatusLimitingReasons
```

## Possible Values

- `FEATURE_NOT_AVAILABLE_IN_COUNTRY_OR_REGION`: The ad feature is not available in one or more targeted countries or regions.
- `ACCOUNT_DOC_APPROVAL_EXPIRED`: Required account documentation has expired and must be resubmitted.
- `ACCOUNT_DOC_APPROVAL_INFECTED`: Required account documentation was flagged as infected.
- `ACCOUNT_DOC_APPROVAL_NOT_SUBMITTED`: Required account documentation has not been submitted.
- `ACCOUNT_DOC_APPROVAL_PENDING`: Account documentation approval is pending.
- `ACCOUNT_DOC_APPROVAL_REJECTED`: Account documentation was rejected.
- `APP_CONTENT_REJECTED`: App content was rejected, limiting delivery in affected markets.
- `APP_CONTENT_REVIEW_PENDING`: App content is under review, limiting delivery in affected markets.
- `APP_DOC_APPROVAL_EXPIRED`: Required app documentation has expired.
- `APP_DOC_APPROVAL_INFECTED`: Required app documentation was flagged as infected.
- `APP_DOC_APPROVAL_NOT_SUBMITTED`: Required app documentation has not been submitted.
- `APP_DOC_APPROVAL_PENDING`: Required app documentation is awaiting approval.
- `APP_DOC_APPROVAL_REJECTED`: Required app documentation was rejected.
- `APP_NOT_ELIGIBLE`: The promoted app is not eligible in some of the targeted markets.
- `APP_NOT_ELIGIBLE_SEARCHADS`: The app is not eligible for App Store ads in some markets.
- `APP_NOT_ELIGIBLE_SUPPLY_SOURCE`: The app is not eligible for the configured supply source in some markets.
- `APP_NOT_ELIGIBLE_SUPPLY_PLACEMENT`: The app is not eligible for the configured supply placement in some markets.
- `APP_LANGUAGE_INCOMPATIBLE`: The app’s supported languages are incompatible with some targeted markets.
- `APP_NOT_PUBLISHED_YET`: The app has not yet been published in all targeted storefronts.
- `SAPIN_LAW_AGENT_UNKNOWN`: Sapin Law compliance agent status is unknown.
- `SAPIN_LAW_FRENCH_BIZ`: Sapin Law restrictions apply to this French business account.
- `SAPIN_LAW_FRENCH_BIZ_UNKNOWN`: French business status under Sapin Law cannot be determined, limiting delivery.
- `BRAND_POLICY_ISSUES`: A brand policy condition is limiting delivery.
- `AD_GROUPS_LIMITED`: One or more ad groups are serving at reduced capacity.

#### Discussion

Unlike [`Campaign.SystemStatusReasons`](./systemstatusreasons-data.typealias.md), these codes describe conditions, such as pending app documentation or brand policy issues, that throttle delivery rather than stop it outright.

##### Example

```json
{
  "systemStatusLimitingReasons": ["AD_GROUPS_LIMITED"]
}
```

See [`CampaignSystemLimitedStatusReason`](../campaignsystemlimitedstatusreason.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaign/systemstatuslimitingreasons-data.typealias)*