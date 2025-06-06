# render(to:)

**Framework**: hvf  
**Kind**: method

Render the current part using the current parameters using the supplied render context If the PartRenderer was created using reusable, all input parameters are intact afterwards; otherwise they are destroyed Returns true if rendering was successful

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func render(to context: @escaping (PartRenderer.Instruction) -> PartRenderer.Action) -> Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/render(to:))*