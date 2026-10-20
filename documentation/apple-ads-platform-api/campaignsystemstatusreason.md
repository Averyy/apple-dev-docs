# CampaignSystemStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

A reason code explaining why a campaign is not currently running.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string CampaignSystemStatusReason
```

## Possible Values

- `PROCESSING`: System and feature state. The campaign was recently created or updated and is still being processed.
- `PAUSED_BY_SYSTEM`: System and feature state. The campaign was paused automatically by the platform.
- `FEATURE_NOT_YET_AVAILABLE`: System and feature state. The campaign uses a feature that is not yet available in all targeted markets.
- `FEATURE_NO_LONGER_AVAILABLE`: System and feature state. The campaign uses a feature that is no longer available.
- `PAUSED_BY_USER`: User and campaign actions. The campaign was paused by a user action.
- `DELETED_BY_USER`: User and campaign actions. The campaign was deleted.
- `USER_REQUESTED_ACCOUNT_SUSPENSION`: User and campaign actions. The account was suspended at the user’s request.
- `CAMPAIGN_DELETED_FOR_BASIC_MSF_MIGRATION`: User and campaign actions. The campaign was deleted as part of a Basic to multi-storefront migration.
- `SCHEDULE_PENDING`: Campaign scheduling. The campaign schedule start date has not yet been reached.
- `SCHEDULE_EXPIRED`: Campaign scheduling. The campaign schedule end date has passed.
- `APP_NOT_ELIGIBLE`: App eligibility. The promoted app is not eligible to run ads.
- `APP_NOT_ELIGIBLE_SEARCHADS`: App eligibility. The promoted app is not eligible for App Store ads.
- `APP_NOT_ELIGIBLE_SUPPLY_PLACEMENT`: App eligibility. The app is not eligible for the campaign’s configured supply placement.
- `APP_NOT_PUBLISHED_YET`: App eligibility. The app has not yet been published on the App Store.
- `APP_NOT_CATEGORIZED`: App eligibility. The promoted app has not been assigned a category on the App Store.
- `APP_SENSITIVE_CONTENT`: App eligibility. The promoted app contains sensitive content that is not eligible to run ads.
- `APP_DOC_APPROVAL_REJECTED`: App eligibility. Required app documentation submitted for approval was rejected.
- `COUNTRIES_OR_REGIONS_NOT_ELIGIBLE`: App eligibility. The targeted countries or regions are not eligible for this campaign type.
- `SAPIN_LAW_AGENT_UNKNOWN`: Sapin Law. The advertising intermediary required under French Sapin Law cannot be identified.
- `SAPIN_LAW_FRENCH_BIZ`: Sapin Law. The campaign is paused because the advertiser is a French business subject to Sapin Law restrictions.
- `SAPIN_LAW_FRENCH_BIZ_UNKNOWN`: Sapin Law. The French business status required under Sapin Law could not be determined.
- `BUDGET_ORDER_EXHAUSTED`: Budget orders. The assigned budget order has been fully spent.
- `BUDGET_ORDER_SCHEDULE_PENDING`: Budget orders. The assigned budget order’s start date has not yet been reached.
- `BUDGET_ORDER_SCHEDULE_EXPIRED`: Budget orders. The assigned budget order’s end date has passed.
- `BUDGET_ORDER_CANCELED`: Budget orders. The assigned budget order was canceled.
- `BUDGET_ORDER_OR_INVOICE_DETAIL_MISSING`: Budget orders. A budget order or required invoice detail is missing.
- `LIFETIME_BUDGET_EXHAUSTED`: Campaign budgets. The campaign’s lifetime budget has been fully spent.
- `MONTHLY_BUDGET_EXHAUSTED`: Campaign budgets. The campaign’s monthly budget has been fully spent.
- `LINE_OF_CREDIT_EXHAUSTED`: Payment and billing. The organization’s line of credit has been exhausted.
- `ORG_PAYMENT_TYPE_DECLINED`: Payment and billing. The organization’s payment method was declined.
- `TAX_VERIFICATION_PENDING`: Payment and billing. Tax verification for the ad account is pending.
- `AD_ACCOUNT_PAYMENT_ISSUES`: Payment and billing. The ad account has an unresolved payment issue.
- `ORG_NO_PAYMENT_METHOD_ON_FILE`: Payment and billing. No payment method is on file for the organization.
- `ORG_CHARGE_BACK_DISPUTED`: Payment and billing. A chargeback dispute is open on the organization’s account.
- `ORG_PAYMENT_METHOD_CHANGED`: Payment and billing. The organization’s payment method was changed.
- `ORG_SUSPENDED_FRAUD`: Organization and account standing. The organization was suspended due to suspected fraudulent activity.
- `ORG_SUSPENDED_POLICY_VIOLATION`: Organization and account standing. The organization was suspended due to a policy violation.
- `CONTENT_PROVIDER_UNLINKED`: Organization and account standing. The content provider associated with the campaign has been unlinked.
- `AD_ACCOUNT_BRAND_DELEGATION_ISSUES`: Organization and account standing. The ad account has unresolved brand delegation issues preventing delivery.
- `AD_GROUPS_MISSING`: Ad groups. The campaign has no ad groups configured.
- `AD_GROUPS_NOT_RUNNING`: Ad groups. All ad groups are paused or otherwise not running.
- `AUTOMATED_KEYWORDS_REQUIRED_AD_GROUP_MISSING`: Ad groups. An ad group required for automated keyword targeting is missing.
- `AUTOMATED_KEYWORDS_REQUIRED_AD_GROUP_NOT_RUNNING`: Ad groups. The ad group required for automated keyword targeting is not running.

#### Discussion

One or more `CampaignSystemStatusReason` values appear in the `systemStatusReasons` array on a [`Campaign`](./campaign.md) when `systemStatus` is `NOT_RUNNING`. These codes are read-only and system-applied. Use them to diagnose delivery issues and determine the appropriate corrective action.

## See Also

- [type CampaignStatus](./campaignstatus.md)
  Advertiser-configurable run state for a campaign.
- [type CampaignSystemStatus](./campaignsystemstatus.md)
  System-evaluated delivery state indicating whether a campaign is currently running.
- [type CampaignDisplayStatus](./campaigndisplaystatus.md)
  Rolled-up delivery state for a campaign, combining advertiser settings and system conditions into a single user-facing label.
- [type CampaignSystemLimitedStatusReason](./campaignsystemlimitedstatusreason.md)
  A reason code indicating that a campaign is running but delivering at reduced capacity.
- [type BillingEvent](./billingevent.md)
  The user interaction that triggers a charge for a campaign.
- [type PromotedObjectType](./promotedobjecttype.md)
  The category of entity that a campaign promotes, determining which values apply.
- [type Currency](./currency.md)
  The currency code used for monetary values in the Apple Ads Platform API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/campaignsystemstatusreason)*