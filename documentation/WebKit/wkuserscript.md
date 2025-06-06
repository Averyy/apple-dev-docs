# WKUserScript

**Framework**: Webkit  
**Kind**: class

A script that the web view injects into a webpage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKUserScript
```

#### Overview

Create a [`WKUserScript`](wkuserscript.md) object when you want to inject custom script code into the pages of your web view. Use this object to specify the JavaScript code to inject, and parameters relating to when and how to inject that code. Before you create the web view, add this object to the [`WKUserContentController`](wkusercontentcontroller.md) object associated with your web view’s configuration.

## Topics

### Creating a User Script Object
- [init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool)](wkuserscript/init(source:injectiontime:formainframeonly:).md)
  Creates a user script object that contains the specified source code and attributes.
- [init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool, in: WKContentWorld)](wkuserscript/init(source:injectiontime:formainframeonly:in:).md)
  Creates a user script object that is scoped to a particular content world.
### Inspecting Script Information
- [var source: String](wkuserscript/source.md)
  The script’s source code.
- [var injectionTime: WKUserScriptInjectionTime](wkuserscript/injectiontime.md)
  The time at which to inject the script into the webpage.
- [enum WKUserScriptInjectionTime](wkuserscriptinjectiontime.md)
  Constants for the times at which to inject script content into a webpage.
- [var isForMainFrameOnly: Bool](wkuserscript/isformainframeonly.md)
  A Boolean value that indicates whether to inject the script into the main frame or all frames.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKUserContentController](wkusercontentcontroller.md)
  An object for managing interactions between JavaScript code and your web view, and for filtering content in your web view.
- [class WKContentRuleListStore](wkcontentruleliststore.md)
  An object that contains the rules for how to load and filter content in the web view.
- [class WKContentWorld](wkcontentworld.md)
  An object that defines a scope of execution for JavaScript code, and which you use to prevent conflicts between different scripts.
- [class WKFrameInfo](wkframeinfo.md)
  An object that contains information about a frame on a webpage.
- [class WKSecurityOrigin](wksecurityorigin.md)
  An object that identifies the origin of a particular resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserscript)*