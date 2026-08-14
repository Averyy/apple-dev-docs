# WKContentWorld.Configuration

**Framework**: WebKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
class Configuration
```

#### Overview

A WKContentWorldConfiguration object allows you to specify custom behavior for a WKContentWorld instance.

WKContentWorldConfiguration allows applications to create WKContentWorld instances which have extra JavaScript capabilities exposed to script in their environment. It does not change any default WebKit behaviors, nor change anything that web page JavaScript can do. Only application JavaScript run in the created `WKContentWorld` will have different capabilities.

For example:

- If your scripts help provide autofill capabilities, you would want to set autofillEnabled to YES.

## Topics

### Initializers
- [init?(coder: NSCoder)](wkcontentworld/configuration/init(coder:).md)
### Instance Properties
- [var allowAccessingClosedShadowRoots: Bool](wkcontentworld/configuration/allowaccessingclosedshadowroots.md)
- [var autofillScriptingEnabled: Bool](wkcontentworld/configuration/autofillscriptingenabled.md)
- [var elementUserInfoEnabled: Bool](wkcontentworld/configuration/elementuserinfoenabled.md)
- [var isInspectable: Bool](wkcontentworld/configuration/isinspectable.md)
- [var jsHandleCreationEnabled: Bool](wkcontentworld/configuration/jshandlecreationenabled.md)
- [var legacyBuiltinOverridesEnabled: Bool](wkcontentworld/configuration/legacybuiltinoverridesenabled.md)
- [var nodeSnapshotCreationEnabled: Bool](wkcontentworld/configuration/nodesnapshotcreationenabled.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [class WKUserScript](wkuserscript.md)
  A script that the web view injects into a webpage.
- [class WKJSHandle](wkjshandle.md)
  A WKJSHandle object contains a reference to a JavaScript object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentworld/configuration)*