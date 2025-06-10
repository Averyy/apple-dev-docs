# rebuild(completionHandler:)

**Framework**: Metal Performance Shaders  
**Kind**: instm

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func rebuild(completionHandler: @escaping MPSAccelerationStructureCompletionHandler)
```

#### Discussion

> ❗ **Important**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func rebuild() async -> MPSAccelerationStructure?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/swift/calling-objective-c-apis-asynchronously).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructure/2980770-rebuild)*