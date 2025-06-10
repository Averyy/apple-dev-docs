# addUserScript(_:)

**Framework**: WebKit  
**Kind**: method

Injects the specified script into the webpage’s content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addUserScript(_ userScript: WKUserScript)
```

## Parameters

- `userScript`: The user script to add to the web view’s current page.

## See Also

- [func removeAllUserScripts()](wkusercontentcontroller/removealluserscripts.md)
  Removes all user scripts from the web view.
- [var userScripts: [WKUserScript]](wkusercontentcontroller/userscripts.md)
  The user scripts associated with the user content controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/adduserscript(_:))*