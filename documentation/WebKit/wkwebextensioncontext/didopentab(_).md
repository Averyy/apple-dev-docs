# didOpenTab(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called by the app when a new tab is opened to fire appropriate events with only this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func didOpenTab(_ newTab: any WKWebExtensionTab)
```

```objc
- (void) didOpenTab:(id<WKWebExtensionTab>) newTab;
```

#### Discussion

This method informs only the specific extension of the opening of a new tab. If the intention is to inform all loaded extensions consistently, you should use the respective method on the extension controller instead.

## Parameters

- `newTab`: The newly opened tab.

## See Also

### Related Documentation
- [var openTabs: Set<AnyHashable>](./opentabs.md)
  A set of open tabs in all open windows that are exposed to this extension.
- [- didCloseTab:windowIsClosing:](./didclosetab_windowisclosing_.md)
  Called by the app when a tab is closed to fire appropriate events with only this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/didopentab(_:))*