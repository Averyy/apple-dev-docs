# contains(_:inCircumferentialRingOfWidth:)

**Framework**: Vision  
**Kind**: method

Returns a Boolean value that indicates whether a ring around this circle’s circumference contains the specified point.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func contains(_ point: NormalizedPoint, inCircumferentialRingOfWidth ringWidth: CGFloat) -> Bool
```

## Parameters

- `point`: The normalized point.
- `ringWidth`: The ring width.

## See Also

- [func contains(NormalizedPoint) -> Bool](normalizedcircle/contains(_:).md)
  Returns a Boolean value that indicates whether this circle, including its boundary, contains the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/normalizedcircle/contains(_:incircumferentialringofwidth:))*