# RecommendationResponseBody.Result

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Usually an array of recommendation, suggestion, or history objects returned by the endpoint. A single object for the Target CPA suggestion query response.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object RecommendationResponseBody.Result
```

#### Discussion

`result` holds the recommendation, suggestion, or history objects an endpoint returns. It’s usually an array, with one entry per matched recommendation or suggestion. The single exception is the target CPA suggestion query response ([`RecommendationQueryTargetCpaSuggestionResponse`](recommendationquerytargetcpasuggestionresponse.md)), where `result` is a single object rather than a list, since that endpoint always returns exactly one suggestion. `result` is absent when the request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/recommendationresponsebody/result-data.dictionary)*