# withLock(_:)

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func withLock<R>(_ body: @Sendable () throws -> R) rethrows -> R where R : Sendable
```

Available when `State` is `()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/withlock(_:)-hple)*