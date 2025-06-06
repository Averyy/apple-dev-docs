# withLock(flags:_:)

**Framework**: os  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func withLock<R>(flags: OSAllocatedUnfairLockFlags, _ body: () throws -> R) rethrows -> R where R : Sendable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/withlock(flags:_:)-u2xj)*