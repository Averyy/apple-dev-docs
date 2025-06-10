# WAError.noRadioResources(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case

An error that occurs if the radio lacks resources.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
case noRadioResources(WAError.NoRadioResourcesDetails)
```

#### Discussion

The radio needs resources to support additional active devices, services, or performance requirements. Close any unneeded network `Connection`s, and stop any unneeded `Browser`s and `Listener`s to free resources, and then retry.

## See Also

- [WAError.NoRadioResourcesDetails](waerror/noradioresourcesdetails.md)
  The optional details describing what resources are lacking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/noradioresources(_:))*