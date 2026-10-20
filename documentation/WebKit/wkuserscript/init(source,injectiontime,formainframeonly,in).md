# init(source:injectionTime:forMainFrameOnly:in:)

**Framework**: WebKit  
**Kind**: init  
**Role**: Initializer

Creates a user script object that is scoped to a particular content world.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool, in contentWorld: WKContentWorld)
```

```objc
- (instancetype) initWithSource:(NSString *) source injectionTime:(WKUserScriptInjectionTime) injectionTime forMainFrameOnly:(BOOL) forMainFrameOnly inContentWorld:(WKContentWorld *) contentWorld;
```

#### Return Value

An initialized user script, or `nil` if initialization failed.

## Parameters

- `source`: The script’s source code.
- `injectionTime`: The time at which to inject the script into the webpage. For a list of possible values, see [`WKUserScriptInjectionTime`](../wkuserscriptinjectiontime.md).
- `forMainFrameOnly`: A Boolean value that indicates whether to inject the script into the main frame. Specify [`true`](../../Swift/true.md) to inject the script only into the main frame, or [`false`](../../Swift/false.md) to inject it into all frames.
- `contentWorld`: The namespace in which to evaluate the script. This parameter doesn’t apply to changes your script makes to the underlying web content, such as the document’s DOM structure. Those changes remain visible to all scripts, regardless of which content world you specify. For more information about content worlds, see [`WKContentWorld`](../wkcontentworld.md).

## See Also

### Creating a User Script Object
- [init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool)](./init%28source,injectiontime,formainframeonly%29.md)
  Creates a user script object that contains the specified source code and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserscript/init(source:injectiontime:formainframeonly:in:))*