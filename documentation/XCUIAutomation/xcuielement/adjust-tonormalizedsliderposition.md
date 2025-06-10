# adjust(toNormalizedSliderPosition:)

**Framework**: XCUIAutomation  
**Kind**: method

Manipulates the UI to change the value the slider displays to a new value, based on a normalized position.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func adjust(toNormalizedSliderPosition normalizedSliderPosition: CGFloat)
```

#### Discussion

A normalized slider value of `0` corresponds to the minimum value of the slider, and `1` corresponds to the maximum value.

> **Note**:  The adjustment is a best effort to move the indicator to the desired position; absolute fidelity isn’t guaranteed.

## See Also

- [var normalizedSliderPosition: CGFloat](xcuielement/normalizedsliderposition.md)
  Returns the position of the slider’s indicator as a normalized value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/adjust(tonormalizedsliderposition:))*