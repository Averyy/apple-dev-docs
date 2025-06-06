# displayName

**Framework**: Webkit  
**Kind**: property

The display name for the data record.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var displayName: String { get }
```

#### Discussion

This property contains identifying information that you to display to users. Typically, the value is the website’s domain name and suffix taken from the host information in the resource’s security origin object. For more information, see [`WKSecurityOrigin`](wksecurityorigin.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord/displayname)*