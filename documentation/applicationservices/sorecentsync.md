# soRecentSync

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var soRecentSync: OSType { get }
```

#### Discussion

Get the message code for the most recentlyencountered synchronization command. If no synchronization commandhas been encountered, 0 is returned. The `speechInfo` parameteris a pointer to a variable of type `OSType`.

This selector works with the `GetSpeechInfo` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sorecentsync)*