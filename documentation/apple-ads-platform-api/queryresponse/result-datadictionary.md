# QueryResponse.Result

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The untyped placeholder item shape for the base `QueryResponse` envelope’s `result` array.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object QueryResponse.Result
```

#### Discussion

`QueryResponse` is a generic envelope meant to be extended, so its `result` array has no properties defined here. Concrete query responses, such as `CampaignQueryResponse` or `KeywordQueryResponse`, declare their own `result` array typed to the resource they return. No endpoint returns this untyped shape directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/queryresponse/result-data.dictionary)*