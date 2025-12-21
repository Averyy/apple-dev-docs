# TaskSequence

**Framework**: WebKit  
**Kind**: associatedtype  
**Required**: Yes

The type of sequence produced by the handler.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
associatedtype TaskSequence : AsyncSequence where Self.TaskSequence.Element == URLSchemeTaskResult, Self.TaskSequence.Failure == any Error
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/urlschemehandler/tasksequence)*