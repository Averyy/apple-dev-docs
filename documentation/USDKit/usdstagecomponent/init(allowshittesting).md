# init(allowsHitTesting:)

**Framework**: USDKit  
**Kind**: init  
**Role**: Initializer

Creates a USDStageComponent in manual mode.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
init(allowsHitTesting: Bool = true)
```

#### Discussion

In manual mode, you control when rendering occurs by calling [`render(_:to:at:)`](./render%28_,to,at%29.md).

## Parameters

- `allowsHitTesting`: Whether to generate collision shapes for hit testing. Defaults to `true`.

## See Also

### Creating a stage component
- [init(USDStage, timeCode: USDStage.TimeCode, allowsHitTesting: Bool) async](./init%28_,timecode,allowshittesting%29.md)
  Creates a USDStageComponent in automatic mode and waits for the first render to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/init(allowshittesting:))*