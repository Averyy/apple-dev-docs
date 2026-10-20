# WKContentWorld.Configuration

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
class Configuration
```

```objc
@interface WKContentWorldConfiguration : NSObject
```

#### Overview

A WKContentWorldConfiguration object allows you to specify custom behavior for a WKContentWorld instance.

WKContentWorldConfiguration allows applications to create WKContentWorld instances which have extra JavaScript capabilities exposed to script in their environment. It does not change any default WebKit behaviors, nor change anything that web page JavaScript can do. Only application JavaScript run in the created `WKContentWorld` will have different capabilities.

For example:

- If your scripts help provide autofill capabilities, you would want to set autofillEnabled to YES.

## Topics

### Initializers
- [init?(coder: NSCoder)](./configuration/init%28coder%29.md)
### Instance Properties
- [var allowAccessingClosedShadowRoots: Bool](./configuration/allowaccessingclosedshadowroots.md)
- [var autofillScriptingEnabled: Bool](./configuration/autofillscriptingenabled.md)
- [var elementUserInfoEnabled: Bool](./configuration/elementuserinfoenabled.md)
- [var isInspectable: Bool](./configuration/isinspectable.md)
- [var jsHandleCreationEnabled: Bool](./configuration/jshandlecreationenabled.md)
- [var legacyBuiltinOverridesEnabled: Bool](./configuration/legacybuiltinoverridesenabled.md)
- [var nodeSnapshotCreationEnabled: Bool](./configuration/nodesnapshotcreationenabled.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Page content
- [class WKUserContentController](../wkusercontentcontroller.md)
  An object for managing interactions between JavaScript code and your web view, and for filtering content in your web view.
- [class WKContentRuleListStore](../wkcontentruleliststore.md)
  An object that contains the rules for how to load and filter content in the web view.
- [class WKContentWorld](../wkcontentworld.md)
  An object that defines a scope of execution for JavaScript code, and which you use to prevent conflicts between different scripts.
- [class WKFrameInfo](../wkframeinfo.md)
  An object that contains information about a frame on a webpage.
- [class WKSecurityOrigin](../wksecurityorigin.md)
  An object that identifies the origin of a particular resource.
- [class WKUserScript](../wkuserscript.md)
  A script that the web view injects into a webpage.
- [class WKJSHandle](../wkjshandle.md)
  A WKJSHandle object contains a reference to a JavaScript object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentworld/configuration)*