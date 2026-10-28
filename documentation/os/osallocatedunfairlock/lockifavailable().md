# lockIfAvailable()

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Attempts to acquire a lock.

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
func lockIfAvailable() -> Bool
```

Available when `State` is `()`.

## Return Value

[`true`](../../Swift/true.md) if successful; otherwise, [`false`](../../Swift/false.md).

## See Also

### Using locks
- [func lock()](./lock%28%29.md)
  Acquires a lock.
- [func unlock()](./unlock%28%29.md)
  Ends the lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/lockifavailable())*