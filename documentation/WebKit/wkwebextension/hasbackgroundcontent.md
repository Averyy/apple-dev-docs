# hasBackgroundContent

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the extension has background content that can run when needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var hasBackgroundContent: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasBackgroundContent;
```

#### Discussion

If this property is `YES`, the extension can run in the background even when no webpages are open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/hasbackgroundcontent)*