# kIONetworkFeatureNoBSDWait

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kIONetworkFeatureNoBSDWait = 0x001
```

## Discussion

Set this bit in the value returned by getFeatures() to disable the automatic wait for "IOBSD" resource by the IONetworkController::start() method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1551508-network/kionetworkfeaturenobsdwait)*