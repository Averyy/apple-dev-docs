# Creative.Eligibility

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Eligibility data summarizing whether the ad creative meets requirements to serve ads.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Creative.Eligibility
```

#### Discussion

Eligibility is read-only and reflects the platform’s current delivery checks for the ad creative across supply sources and placements. See [`CreativeEligibility`](creativeeligibility.md) for the full field reference.

## Properties

- `status` (string): The overall eligibility status. Values: `ELIGIBLE`, `INELIGIBLE`. Read-only.
- `allowedGroups` (CreativeEligibility.AllowedGroups): The supply sources and placements where this ad creative is eligible to serve. Read-only.
- `blockedGroups` (CreativeEligibility.BlockedGroups): The supply sources and placements where this ad creative is not eligible to serve, along with the blocking reason. Read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creative/eligibility-data.dictionary)*