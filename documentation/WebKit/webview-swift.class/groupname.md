# groupName

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s group name.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var groupName: String! { get set }
```

```objc
@property (nonatomic, copy) NSString * groupName;
```

#### Discussion

You might use this to set the group name of a `WebView` object after it is loaded from a nib file.

## See Also

### Related Documentation
- [init!(frame: NSRect, frameName: String!, groupName: String!)](./init%28frame,framename,groupname%29.md)
  Initializes the receiver with a frame rectangle, frame name, and group name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/groupname)*