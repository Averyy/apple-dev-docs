# init(source:injectionTime:forMainFrameOnly:)

**Framework**: WebKit  
**Kind**: init  
**Role**: Initializer

Creates a user script object that contains the specified source code and attributes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool)
```

```objc
- (instancetype) initWithSource:(NSString *) source injectionTime:(WKUserScriptInjectionTime) injectionTime forMainFrameOnly:(BOOL) forMainFrameOnly;
```

## Return Value

An initialized user script, or `nil` if initialization failed.

## Discussion

This method sets the script’s content world to the object in the [`page`](../wkcontentworld/page.md) property of [`WKContentWorld`](../wkcontentworld.md).

## Parameters

- `source`: The script’s source code.
- `injectionTime`: The time at which to inject the script into the webpage. For a list of possible values, see [`WKUserScriptInjectionTime`](../wkuserscriptinjectiontime.md).
- `forMainFrameOnly`: A Boolean value that indicates whether to inject the script into the main frame. Specify [`true`](../../Swift/true.md) to inject the script only into the main frame, or [`false`](../../Swift/false.md) to inject it into all frames.

## See Also

### Creating a User Script Object
- [init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool, in: WKContentWorld)](./init%28source,injectiontime,formainframeonly,in%29.md)
  Creates a user script object that is scoped to a particular content world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserscript/init(source:injectiontime:formainframeonly:))*