# init(_:)

**Framework**: Siri Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a loader that supplies the scenarios a builder closure produces, in the order written.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
init(@SiriScenarioLoaderBuilder _ content: () -> SiriScenarioLoader)
```

## See Also

### Creating a loader
- [enum SiriScenarioLoaderBuilder](../siriscenarioloaderbuilder.md)
  A result builder that collects scenarios into one dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenarioloader/init(_:))*