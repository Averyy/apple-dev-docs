# contains(_:caseSensitive:)

**Framework**: Siri Evaluations  
**Kind**: method  
**Role**: Type Method

Returns a check that the reply’s text contains the value.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
static func contains(_ value: String, caseSensitive: Bool = true) -> SiriResponse.Text
```

## Discussion

Case-sensitive unless `caseSensitive` is `false`. Ignoring case suits a word Siri may capitalize or not (`honeymoon`), where a flight number or a name the person gave is better checked exactly. `value` is always plain text, never a pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriresponse/text/contains(_:casesensitive:))*