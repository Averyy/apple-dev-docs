# plugInView(withArguments:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Creates a new plug-in view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
static func plugInView(withArguments arguments: [AnyHashable : Any]!) -> NSView!
```

#### Return Value

The created view.

#### Discussion

This method returns an `NSView` object that conforms to the `WebPlugIn` informal protocol. The arguments dictionary should be specified by the keys and objects described in `Constants`. This method is required.

## Parameters

- `arguments`: Arguments used in creating the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpluginviewfactory/pluginview(witharguments:))*