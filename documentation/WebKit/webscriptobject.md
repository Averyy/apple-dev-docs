# WebScriptObject

**Framework**: WebKit  
**Kind**: class

A `WebScriptObject` object is an Objective-C wrapper for a scripting object passed to your application from the scripting environment.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class WebScriptObject
```

#### Overview

You can not create a `WebScriptObject` object directly. You get a window `WebScriptObject` object by sending [`windowScriptObject`](webview-swift.class/windowscriptobject.md) to your `WebView` object.

You can use key-value coding methods—for example, `setValue:forKey:` and `valueForKey:`—to get and set properties of a `WebScriptObject` object. You can also access properties by index using the [`setWebScriptValueAt(_:value:)`](webscriptobject/setwebscriptvalueat(_:value:).md) and [`webScriptValue(at:)`](webscriptobject/webscriptvalue(at:).md) methods. Use the [`removeWebScriptKey(_:)`](webscriptobject/removewebscriptkey(_:).md) method to remove a scripting object property.

Not all properties and methods of a class are exported. Use the [`setValue(_:forUndefinedKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/setValue(_:forUndefinedKey:)) and [`value(forUndefinedKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/value(forUndefinedKey:)) methods to intercept access to properties that are not exported. Similarly, use the [`invokeUndefinedMethod(fromWebScript:withArguments:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/invokeUndefinedMethod(fromWebScript:withArguments:)) method to intercept method invocations that are not exported.

If you want access to properties and methods defined in your own classes, use the methods in the WebScripting informal protocol to specify the properties and methods the class should export to WebKit’s JavaScript environment.

Use the [`callWebScriptMethod(_:withArguments:)`](webscriptobject/callwebscriptmethod(_:witharguments:).md) and [`evaluateWebScript(_:)`](webscriptobject/evaluatewebscript(_:).md) methods to execute scripts in the scripting environment.

## Topics

### Getting and setting properties
- [func jsObject() -> JSObjectRef!](webscriptobject/jsobject.md)
  Returns the JavaScript object corresponding to the receiver.
- [func removeWebScriptKey(String!)](webscriptobject/removewebscriptkey(_:).md)
  Removes a property from a scripting environment.
- [func webScriptValue(at: UInt32) -> Any!](webscriptobject/webscriptvalue(at:).md)
  Returns the value of a property at the specified index.
- [func setWebScriptValueAt(UInt32, value: Any!)](webscriptobject/setwebscriptvalueat(_:value:).md)
  Sets the value of a property at the specified index.
### Executing scripts
- [func callWebScriptMethod(String!, withArguments: [Any]!) -> Any!](webscriptobject/callwebscriptmethod(_:witharguments:).md)
  Returns the result of executing a method in the scripting environment.
- [func evaluateWebScript(String!) -> Any!](webscriptobject/evaluatewebscript(_:).md)
  Returns the result of evaluating a script in the scripting environment.
### Raising exceptions
- [class func throwException(String!) -> Bool](webscriptobject/throwexception(_:).md)
  Raises an exception in the current script execution context.
- [func setException(String!)](webscriptobject/setexception(_:).md)
  Raises a scripting environment exception in the context of the current object.
### Getting a string representation
- [func stringRepresentation() -> String!](webscriptobject/stringrepresentation.md)
  Returns a string representation of the receiver.
### Instance Methods
- [func jsValue() -> JSValue!](webscriptobject/jsvalue.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [DOMObject](domobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [WebKit DOM Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)
- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
- [WebScripting](../ObjectiveC/webscripting.md)
  `WebScripting` is an informal protocol that defines methods that classes can implement to export their interfaces to a WebScript environment such as JavaScript.
- [class WebUndefined](webundefined.md)
  `WebUndefined` objects are simply used to represent the JavaScript “undefined” value in methods when bridging between JavaScript and Objective-C. For example, if you invoke a JavaScript function that returns the JavaScript “undefined” value, then a `WebUndefined` object is returned to the Objective-C calling context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webscriptobject)*