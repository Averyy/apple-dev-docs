# RecommendationResponseErrorDetail.Info

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Additional context that supplements the error message, varying by endpoint and error type.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationResponseErrorDetail.Info
```

#### Discussion

`info` supplements the parent detail’s `message` with structured context, such as the field name, the invalid value, or acceptable alternatives. Its shape depends on the endpoint and the error condition. For example, a `MISSING_REQUIRED_FILTER` error includes the missing filter’s field name and location, as in `{"field": "promotedObjectId", "location": "filters"}`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationresponseerrordetail/info-data.dictionary)*