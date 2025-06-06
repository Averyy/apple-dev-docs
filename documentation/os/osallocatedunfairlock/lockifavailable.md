# lockIfAvailable()

**Framework**: os  
**Kind**: method

Attempts to acquire a lock.

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
func lockIfAvailable() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func lock()](osallocatedunfairlock/lock.md)
  Acquires a lock.
- [func unlock()](osallocatedunfairlock/unlock.md)
  Ends the lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/lockifavailable())*