# coordinate(withNormalizedOffset:)

**Framework**: Xcuiautomation  
**Kind**: method

Creates and returns a new coordinate with a normalized offset.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func coordinate(withNormalizedOffset normalizedOffset: CGVector) -> XCUICoordinate
```

#### Discussion

The coordinate’s screen point is computed by adding `normalizedOffset` multiplied by the size of the element’s frame to the origin of the element’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/coordinate(withnormalizedoffset:))*