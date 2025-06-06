# withLockUnchecked(_:)

**Framework**: os  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func withLockUnchecked<R>(_ body: (inout State) throws -> R) rethrows -> R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/withlockunchecked(_:)-7qywq)*