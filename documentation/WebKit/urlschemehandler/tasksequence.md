# TaskSequence

**Framework**: WebKit  
**Kind**: associatedtype  
**Required**: Yes

The type of sequence produced by the handler.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
associatedtype TaskSequence : AsyncSequence where Self.TaskSequence.Element == URLSchemeTaskResult, Self.TaskSequence.Failure == any Error
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/urlschemehandler/tasksequence)*