# withLockUnchecked(flags:_:)

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
func withLockUnchecked<R>(flags: OSAllocatedUnfairLockFlags, _ body: (inout State) throws -> R) rethrows -> R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/withlockunchecked(flags:_:)-8cv64)*