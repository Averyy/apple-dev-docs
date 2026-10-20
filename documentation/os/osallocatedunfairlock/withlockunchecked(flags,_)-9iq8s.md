# withLockUnchecked(flags:_:)

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func withLockUnchecked<R>(flags: OSAllocatedUnfairLockFlags, _ body: () throws -> R) rethrows -> R
```

Available when `State` is `()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/withlockunchecked(flags:_:)-9iq8s)*