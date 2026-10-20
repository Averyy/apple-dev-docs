# addUserScript(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Injects the specified script into the webpage’s content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func addUserScript(_ userScript: WKUserScript)
```

```objc
- (void) addUserScript:(WKUserScript *) userScript;
```

## Parameters

- `userScript`: The user script to add to the web view’s current page.

## See Also

### Adding and Removing Custom Scripts
- [func removeAllUserScripts()](./removealluserscripts%28%29.md)
  Removes all user scripts from the web view.
- [var userScripts: [WKUserScript]](./userscripts.md)
  The user scripts associated with the user content controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/adduserscript(_:))*