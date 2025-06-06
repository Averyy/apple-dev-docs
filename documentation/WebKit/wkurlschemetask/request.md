# request

**Framework**: Webkit  
**Kind**: property  
**Required**: Yes

Information about the resource to load.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var request: URLRequest { get }
```

#### Discussion

Use the value of this property to get the URL of the requested resource, and any additional details. It is safe to retrieve the value of this property even after WebKit cancels the load request by calling your handler’s [`webView(_:stop:)`](wkurlschemehandler/webview(_:stop:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkurlschemetask/request)*