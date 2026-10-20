# default

**Framework**: os  
**Kind**: property  
**Role**: Type Property

The shared default log.

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
static let `default`: OSLog
```

#### Discussion

Passing this constant to an `os_log` function causes the system to log a message with the system’s standard behavior.

## See Also

### Getting the Shared Logs
- [static let disabled: OSLog](./disabled.md)
  The shared disabled log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslog/default)*