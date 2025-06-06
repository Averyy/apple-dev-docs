# MPSPurgeableState.allocationDeferred

**Framework**: Metal Performance Shaders  
**Kind**: enumelt

The image’s underlying texture hasn’t been allocated yet. Attempts to set another purgeable state using the [`setPurgeableState(_:)`](mpsimage/1648820-setpurgeablestate.md) method will be ignored.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case allocationDeferred = 0
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpspurgeablestate/allocationdeferred)*