# AdGroup.SystemStatusLimitingReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Reasons that limit delivery for an ad group without fully stopping it.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdGroup.SystemStatusLimitingReasons
```

## Possible Values

- `LOCATION_POLICY_ISSUES`: The ad group’s location targeting contains areas with policy restrictions.
- `LOCATION_GROUP_ISSUES`: The ad group’s location group targeting has issues that limit delivery.
- `ADS_LIMITED`: One or more ads in the ad group are limited, reducing overall delivery.

#### Discussion

These reasons can stem from the ad group’s own location targeting or cascade up from limited ads within it, as with `ADS_LIMITED`.

##### Example

```json
{
  "systemStatusLimitingReasons": [
    "ADS_LIMITED"
  ]
}
```

See [`AdGroupSystemLimitedStatusReason`](../adgroupsystemlimitedstatusreason.md) for the full field reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/systemstatuslimitingreasons-data.typealias)*