# normalizedSliderPosition

**Framework**: XCUIAutomation  
**Kind**: property

Returns the position of the slider’s indicator as a normalized value.

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
var normalizedSliderPosition: CGFloat { get }
```

#### Discussion

A value of `0` corresponds to the minimum value of the slider, and `1` corresponds to its maximum value.

## See Also

- [func adjust(toNormalizedSliderPosition: CGFloat)](xcuielement/adjust(tonormalizedsliderposition:).md)
  Manipulates the UI to change the value the slider displays to a new value, based on a normalized position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/normalizedsliderposition)*