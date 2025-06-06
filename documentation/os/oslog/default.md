# default

**Framework**: os  
**Kind**: property

The shared default log.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
static let `default`: OSLog
```

#### Discussion

Passing this constant to an `os_log` function causes the system to log a message with the system’s standard behavior.

## See Also

- [static let disabled: OSLog](oslog/disabled.md)
  The shared disabled log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslog/default)*