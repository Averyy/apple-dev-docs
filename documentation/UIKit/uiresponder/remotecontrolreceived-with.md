# remoteControlReceived(with:)

**Framework**: UIKit  
**Kind**: method

Tells the object when a remote-control event is received.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func remoteControlReceived(with event: UIEvent?)
```

#### Discussion

Remote-control events originate as commands from external accessories, including headsets. An app responds to these commands by controlling audio or video media presented to the user. The receiving responder object should examine the [`subtype`](uievent/subtype.md) of `event` to determine the intended command — for example,  ([`UIEvent.EventSubtype.remoteControlPlay`](uievent/eventsubtype/remotecontrolplay.md)) — and then proceed accordingly.

To allow delivery of remote-control events, you must call the [`beginReceivingRemoteControlEvents()`](uiapplication/beginreceivingremotecontrolevents().md) method of [`UIApplication`](uiapplication.md). To turn off delivery of remote-control events, call the [`endReceivingRemoteControlEvents()`](uiapplication/endreceivingremotecontrolevents().md) method.

## Parameters

- `event`: An event object encapsulating a remote-control command. Remote-control events have a type of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/remotecontrolreceived(with:))*