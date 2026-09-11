# waitForRenderCompletion(on:)

**Framework**: USDKit  
**Kind**: method

Waits for automatic rendering to complete.

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
static func waitForRenderCompletion(on entity: Entity) async -> USDStageComponent.RenderResult
```

#### Return Value

The result of the render operation.

#### Discussion

If the entity does not have a `USDStageComponent` attached, or if the attached component is in manual mode, the result is `.failed`.

## Parameters

- `entity`: The entity with a `USDStageComponent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstagecomponent/waitforrendercompletion(on:))*