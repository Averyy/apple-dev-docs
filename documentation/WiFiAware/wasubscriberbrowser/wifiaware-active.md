# wifiAware(_:active:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Setup a `NetworkBrowser` to subscribe to Wi-Fi Aware services on selected, paired devices.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
static func wifiAware(_ action: WASubscriberBrowser.Action, active requestedDuration: Duration? = nil) -> Self
```

#### Return Value

A new `BrowserProvider` containing the `.wifiAware()` instruction that will configure a `NetworkBrowser` as a Wi-Fi Aware subscriber.

#### Discussion

Example:

```swift
NetworkBrowser(for: .wifiAware(.connecting(to:.selected(devices), from:service)) )
```

## Parameters

- `action`: The specific Wi-Fi Aware operation to perform, and the service & devices to perform it on.
- `requestedDuration`: Optional duration requested to keep the   subscribing. The default value of   instructs the system to stay active for long enough to guarantee the action completes with all nearby target devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/wifiaware(_:active:))*