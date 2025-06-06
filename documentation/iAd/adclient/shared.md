# shared()

**Framework**: Iad  
**Kind**: method

Gets an instance of ADClient.

## Declaration

```swift
class func shared() -> ADClient
```

#### Return Value

An instance of ADClient.

#### Discussion

Use the `ADClient` instance to obtain attribution details.

> **Note**:  This method no longer returns a singleton. This change results in a small savings in memory usage by freeing up objects that aren’t required after the request for attribution details completes.

```swift
ADClient.shared.requestAttributionDetails()
```

```objc
[[ADClient SharedClient] requestAttributionDetailsWithBlock:]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iad/adclient/shared())*