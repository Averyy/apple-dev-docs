# coordinateSpace(on:at:timeCode:)

**Framework**: USDKit  
**Kind**: method

Returns a coordinate space anchored to the closest rendered ancestor of `path`.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
static func coordinateSpace(on root: Entity, at path: USDLayer.Path, timeCode: USDStage.TimeCode? = nil) -> some CoordinateSpace3DFloat
```

## Parameters

- `root`: The entity hosting the `USDStageComponent`.
- `path`: The prim path to map.
- `timeCode`: Time code at which to evaluate. Defaults to `component.timeCode`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/coordinatespace(on:at:timecode:))*