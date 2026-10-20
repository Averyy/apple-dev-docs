# lock()

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Acquires a lock.

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
func lock()
```

Available when `State` is `()`.

## See Also

### Using locks
- [func lockIfAvailable() -> Bool](./lockifavailable%28%29.md)
  Attempts to acquire a lock.
- [func unlock()](./unlock%28%29.md)
  Ends the lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/lock())*