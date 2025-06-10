# init(source:injectionTime:forMainFrameOnly:in:)

**Framework**: WebKit  
**Kind**: init

Creates a user script object that is scoped to a particular content world.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool, in contentWorld: WKContentWorld)
```

#### Return Value

An initialized user script, or `nil` if initialization failed.

## Parameters

- `source`: The script’s source code.
- `injectionTime`: The time at which to inject the script into the webpage. For a list of possible values, see  .
- `forMainFrameOnly`: A Boolean value that indicates whether to inject the script into the main frame. Specify   to inject the script only into the main frame, or   to inject it into all frames.
- `contentWorld`: The namespace in which to evaluate the script. This parameter doesn’t apply to changes your script makes to the underlying web content, such as the document’s DOM structure. Those changes remain visible to all scripts, regardless of which content world you specify. For more information about content worlds, see  .

## See Also

- [init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool)](wkuserscript/init(source:injectiontime:formainframeonly:).md)
  Creates a user script object that contains the specified source code and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserscript/init(source:injectiontime:formainframeonly:in:))*