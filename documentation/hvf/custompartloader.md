# CustomPartLoader

**Framework**: hvf  
**Kind**: typealias

Closure which loads parts from an arbitrary source The first parameter is the part index which uniquely identifiers a part; these are assigned by the loader The second parameter is a PartGenerator the loader uses to get a ShapeWriter or CompositeWriter to create the requested part The result is the generated part, passed back in a PartResult

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
typealias CustomPartLoader = (Int, any PartGenerator) -> PartResult
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/custompartloader)*