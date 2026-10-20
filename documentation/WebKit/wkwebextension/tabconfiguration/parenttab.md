# parentTab

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

Indicates the parent tab with which the tab should be related.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var parentTab: (any WKWebExtensionTab)? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) id<WKWebExtensionTab> parentTab;
```

#### Discussion

If this property is `nil`, no parent tab was specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/tabconfiguration/parenttab)*