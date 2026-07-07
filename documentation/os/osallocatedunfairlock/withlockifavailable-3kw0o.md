# withLockIfAvailable(_:)

**Framework**: os  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func withLockIfAvailable<R>(_ body: @Sendable (inout State) throws -> R) rethrows -> R? where R : Sendable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/withlockifavailable(_:)-3kw0o)*