# withUnsafePointer(_:)

**Framework**: Vision  
**Kind**: method

Invokes the given closure with a pointer to the given argument.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func withUnsafePointer<R>(_ body: (UnsafeRawPointer) -> R) -> R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/opticalflowobservation/withunsafepointer(_:))*