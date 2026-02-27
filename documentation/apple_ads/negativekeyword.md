# NegativeKeyword

**Framework**: Apple Ads  
**Kind**: dictionary

Negative keyword parameters to use in requests and responses.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object NegativeKeyword
```

## Properties

- `adGroupId` (int64): The unique identifier of the ad group that the negative keywords belong to. For campaign negative keyword endpoints, the value is `null`. You can use the EQUALS and IN selector [`Condition`](condition.md) operators with [`Find Campaign Negative Keywords`](find-campaign-negative-keywords.md).
- `campaignId` (int64): The unique identifier of the campaign that the negative keywords belong to. You can use the EQUALS and IN selector [`Condition`](condition.md) operators with [`Find Campaign Negative Keywords`](find-campaign-negative-keywords.md).
- `deleted` (boolean): An indicator of whether the negative keyword is soft-deleted.
- `id` (int64): A unique identifier for the negative keyword. You can use the EQUALS and IN selector [`Condition`](condition.md) operators with [`Find Campaign Negative Keywords`](find-campaign-negative-keywords.md).
- `matchType` (string) *(required)*: An automated keyword and bidding strategy. Match type can be either `Broad` or `Exact`. See [`Ad Groups`](ad-groups.md) for Search Match use cases. | **Value** | **Description** |
| --- | --- |
| `Broad` | Use this value to ensure your ads don’t run on relevant, close variants of a keyword, such as singulars, plurals, misspellings, synonyms, related searches, and phrases that include that term (fully or partially). |
| `Exact` | Use this value for the most control over searches you don’t want your ad to appear in. You can target a specific term and its close variants, such as common misspellings and plurals. |
- `modificationTime` (date-time): The date and time of the most recent modification of the object. You can use the EQUALS and IN selector [`Condition`](condition.md) operators  with [`Find Campaign Negative Keywords`](find-campaign-negative-keywords.md).
- `status` (string): The user-controlled status to enable or pause the keyword.
- `text` (string) *(required)*: The word or phrase to negate in App Store user searches from showing your ad.

## See Also

- [object Keyword](keyword.md)
  Targeting keyword parameters to use in requests and responses.
- [object KeywordResponse](keywordresponse.md)
  A container for the targeting keywords response body.
- [object KeywordListResponse](keywordlistresponse.md)
  The response details of targeting keyword requests.
- [object KeywordUpdateRequest](keywordupdaterequest.md)
  Targeting keyword parameters to use in requests and responses.
- [object NegativeKeywordResponse](negativekeywordresponse.md)
  A container for the negative keyword response body.
- [object NegativeKeywordListResponse](negativekeywordlistresponse.md)
  The response details of negative keyword requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/negativekeyword)*