# waitForRenderCompletion(on:)

**Framework**: USDKit  
**Kind**: method

Waits for automatic rendering to complete.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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