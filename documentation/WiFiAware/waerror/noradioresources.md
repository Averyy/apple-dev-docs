# WAError.noRadioResources(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case

An error that occurs if the radio lacks resources.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case noRadioResources(WAError.NoRadioResourcesDetails)
```

#### Discussion

The radio needs resources to support additional active devices, services, or performance requirements. Close any unneeded network `NetworkConnection`s, and stop any unneeded `NetworkBrowser`s and `NetworkListener`s to free resources, and then retry.

## See Also

- [WAError.NoRadioResourcesDetails](waerror/noradioresourcesdetails.md)
  The optional details describing what resources are lacking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/noradioresources(_:))*