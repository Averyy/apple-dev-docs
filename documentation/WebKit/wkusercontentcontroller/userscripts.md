# userScripts

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The user scripts associated with the user content controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var userScripts: [WKUserScript] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<WKUserScript *> * userScripts;
```

## See Also

### Adding and Removing Custom Scripts
- [func addUserScript(WKUserScript)](./adduserscript%28_%29.md)
  Injects the specified script into the webpage’s content.
- [func removeAllUserScripts()](./removealluserscripts%28%29.md)
  Removes all user scripts from the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/userscripts)*