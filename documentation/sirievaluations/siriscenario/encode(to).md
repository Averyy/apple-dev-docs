# encode(to:)

**Framework**: Siri Evaluations  
**Kind**: method  
**Role**: Instance Method

The scenario’s own fields, plus the utterances as one line.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

## Discussion

The line is written as `input`. The evaluation runner stores the whole scenario in the report’s Input column, and Xcode shows a sample’s `input` field when it has one. Without it, Xcode prints the scenario’s entire JSON. Decoding is unchanged (it is synthesized, over `CodingKeys`), so a scenario file with or without `input` reads the same.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenario/encode(to:))*