# WKContentWorldConfiguration

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
class WKContentWorldConfiguration
```

#### Overview

A WKContentWorldConfiguration object allows you to specify custom behavior for a WKContentWorld instance.

WKContentWorldConfiguration allows applications to create WKContentWorld instances which have extra JavaScript capabilities exposed to script in their environment. It does not change any default WebKit behaviors, nor change anything that web page JavaScript can do. Only application JavaScript run in the created `WKContentWorld` will have different capabilities.

For example:

- If your scripts help provide autofill capabilities, you would want to set autofillEnabled to YES.

## Topics

### Initializers
- [init?(coder: NSCoder)](wkcontentworldconfiguration/init(coder:).md)
### Instance Properties
- [var autofillScriptingEnabled: Bool](wkcontentworldconfiguration/autofillscriptingenabled.md)
- [var elementUserInfoEnabled: Bool](wkcontentworldconfiguration/elementuserinfoenabled.md)
- [var isInspectable: Bool](wkcontentworldconfiguration/isinspectable.md)
- [var jsHandleCreationEnabled: Bool](wkcontentworldconfiguration/jshandlecreationenabled.md)
- [var legacyBuiltinOverridesEnabled: Bool](wkcontentworldconfiguration/legacybuiltinoverridesenabled.md)
- [var nodeSerializationEnabled: Bool](wkcontentworldconfiguration/nodeserializationenabled.md)
- [var openClosedShadowRootsEnabled: Bool](wkcontentworldconfiguration/openclosedshadowrootsenabled.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class WKJSScriptingBuffer](wkjsscriptingbuffer.md)
  A WKJSScriptingBuffer object exposes an application controlled data buffer to JavaScript.
- [class WKJSSerializedNode](wkjsserializednode.md)
  A `WKJSSerializedNode` object contains the serialized representation of a DOM node


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentworldconfiguration)*