# keyMissedKeywordAttr

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var keyMissedKeywordAttr: AEKeyword { get }
```

#### Discussion

Keyword for first required parameter remaining in an Apple event. (Read only.)

After extracting all known Apple event parameters from an event, your handler should check whether the `keyMissedKeywordAttr` attribute exists. If so, your handler has not retrieved all the parameters that the source application considered to be required, and it should return an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/keymissedkeywordattr)*