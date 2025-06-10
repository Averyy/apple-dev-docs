# kIONetworkFeatureNoBSDWait

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
kIONetworkFeatureNoBSDWait = 0x001
```

#### Discussion

Set this bit in the value returned by getFeatures() to disable the automatic wait for "IOBSD" resource by the IONetworkController::start() method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeaturenobsdwait)*