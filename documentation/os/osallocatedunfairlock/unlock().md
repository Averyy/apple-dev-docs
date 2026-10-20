# unlock()

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Ends the lock.

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
func unlock()
```

Available when `State` is `()`.

## See Also

### Using locks
- [func lock()](./lock%28%29.md)
  Acquires a lock.
- [func lockIfAvailable() -> Bool](./lockifavailable%28%29.md)
  Attempts to acquire a lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/unlock())*