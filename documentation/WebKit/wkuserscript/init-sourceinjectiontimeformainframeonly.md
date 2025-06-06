# init(source:injectionTime:forMainFrameOnly:)

**Framework**: Webkit  
**Kind**: init

Creates a user script object that contains the specified source code and attributes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool)
```

#### Return Value

An initialized user script, or `nil` if initialization failed.

#### Discussion

This method sets the script’s content world to the object in the [`page`](wkcontentworld/page.md) property of [`WKContentWorld`](wkcontentworld.md).

## Parameters

- `source`: The script’s source code.
- `injectionTime`: The time at which to inject the script into the webpage. For a list of possible values, see  .
- `forMainFrameOnly`: A Boolean value that indicates whether to inject the script into the main frame. Specify   to inject the script only into the main frame, or   to inject it into all frames.

## See Also

- [init(source: String, injectionTime: WKUserScriptInjectionTime, forMainFrameOnly: Bool, in: WKContentWorld)](wkuserscript/init(source:injectiontime:formainframeonly:in:).md)
  Creates a user script object that is scoped to a particular content world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserscript/init(source:injectiontime:formainframeonly:))*