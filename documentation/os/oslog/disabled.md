# disabled

**Framework**: os  
**Kind**: property  
**Role**: Type Property

The shared disabled log.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS
- watchOS 3.0+

## Declaration

```swift
static let disabled: OSLog
```

## Discussion

Passing this constant to an `os_log` function prevents the system from logging a message.

## See Also

### Getting the Shared Logs
- [static let `default`: OSLog](./default.md)
  The shared default log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslog/disabled)*