# isInert(ignoringChildren:)

**Framework**: USDKit  
**Kind**: method

Returns a Boolean value that indicates whether the spec contains no authored data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func isInert(ignoringChildren: Bool = false) -> Bool
```

#### Return Value

`true` if the spec has no authored data.

## Parameters

- `ignoringChildren`: Pass `true` to skip child specifier lists when evaluating inertness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/spec/fieldcollection/isinert(ignoringchildren:))*