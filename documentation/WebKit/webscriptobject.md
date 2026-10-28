# WebScriptObject

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

A `WebScriptObject` object is an Objective-C wrapper for a scripting object passed to your application from the scripting environment.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
class WebScriptObject
```

```objc
@interface WebScriptObject : NSObject
```

## Overview

You can not create a `WebScriptObject` object directly. You get a window `WebScriptObject` object by sending [`windowScriptObject`](./webview-swift.class/windowscriptobject.md) to your `WebView` object.

You can use key-value coding methods—for example, `setValue:forKey:` and `valueForKey:`—to get and set properties of a `WebScriptObject` object. You can also access properties by index using the [`setWebScriptValueAt(_:value:)`](./webscriptobject/setwebscriptvalueat%28_,value%29.md) and [`webScriptValue(at:)`](./webscriptobject/webscriptvalue%28at%29.md) methods. Use the [`removeWebScriptKey(_:)`](./webscriptobject/removewebscriptkey%28_%29.md) method to remove a scripting object property.

Not all properties and methods of a class are exported. Use the [`setValue(_:forUndefinedKey:)`](../ObjectiveC/nsobject-swift.class/setvalue%28_,forundefinedkey%29.md) and [`value(forUndefinedKey:)`](../ObjectiveC/nsobject-swift.class/value%28forundefinedkey%29.md) methods to intercept access to properties that are not exported. Similarly, use the [`invokeUndefinedMethod(fromWebScript:withArguments:)`](../ObjectiveC/nsobject-swift.class/invokeundefinedmethod%28fromwebscript,witharguments%29.md) method to intercept method invocations that are not exported.

If you want access to properties and methods defined in your own classes, use the methods in the WebScripting informal protocol to specify the properties and methods the class should export to WebKit’s JavaScript environment.

Use the [`callWebScriptMethod(_:withArguments:)`](./webscriptobject/callwebscriptmethod%28_,witharguments%29.md) and [`evaluateWebScript(_:)`](./webscriptobject/evaluatewebscript%28_%29.md) methods to execute scripts in the scripting environment.

## Topics

### Getting and setting properties
- [func jsObject() -> JSObjectRef!](./webscriptobject/jsobject%28%29.md)
  Returns the JavaScript object corresponding to the receiver.
- [func removeWebScriptKey(String!)](./webscriptobject/removewebscriptkey%28_%29.md)
  Removes a property from a scripting environment.
- [func webScriptValue(at: UInt32) -> Any!](./webscriptobject/webscriptvalue%28at%29.md)
  Returns the value of a property at the specified index.
- [func setWebScriptValueAt(UInt32, value: Any!)](./webscriptobject/setwebscriptvalueat%28_,value%29.md)
  Sets the value of a property at the specified index.
### Executing scripts
- [func callWebScriptMethod(String!, withArguments: [Any]!) -> Any!](./webscriptobject/callwebscriptmethod%28_,witharguments%29.md)
  Returns the result of executing a method in the scripting environment.
- [func evaluateWebScript(String!) -> Any!](./webscriptobject/evaluatewebscript%28_%29.md)
  Returns the result of evaluating a script in the scripting environment.
### Raising exceptions
- [class func throwException(String!) -> Bool](./webscriptobject/throwexception%28_%29.md)
  Raises an exception in the current script execution context.
- [func setException(String!)](./webscriptobject/setexception%28_%29.md)
  Raises a scripting environment exception in the context of the current object.
### Getting a string representation
- [func stringRepresentation() -> String!](./webscriptobject/stringrepresentation%28%29.md)
  Returns a string representation of the receiver.
### Instance Methods
- [func jsValue() -> JSValue!](./webscriptobject/jsvalue%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [DOMObject](./domobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
### Incorporating Scripts (Legacy)
- [WebScripting](../ObjectiveC/webscripting.md)
  `WebScripting` is an informal protocol that defines methods that classes can implement to export their interfaces to a WebScript environment such as JavaScript.
- [class WebUndefined](./webundefined.md)
  `WebUndefined` objects are simply used to represent the JavaScript “undefined” value in methods when bridging between JavaScript and Objective-C. For example, if you invoke a JavaScript function that returns the JavaScript “undefined” value, then a `WebUndefined` object is returned to the Objective-C calling context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject)*