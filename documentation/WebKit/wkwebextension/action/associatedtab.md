# associatedTab

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The tab that this action is associated with, or `nil` if it’s the default action.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
weak var associatedTab: (any WKWebExtensionTab)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<WKWebExtensionTab> associatedTab;
```

#### Discussion

When this property is `nil`, it indicates that the action is the default action and not associated with a specific tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/action/associatedtab)*