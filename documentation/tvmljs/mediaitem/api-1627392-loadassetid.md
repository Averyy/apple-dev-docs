# loadAssetID

**Framework**: TVMLKit JS  
**Kind**: instp

A callback function used to load the asset identifier for an item.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
readonly attribute Object loadAssetID;
```

#### Discussion

This attribute must be set if FairPlay Streaming is supported. This attribute must be assigned to a function that takes two parameters, `url` and `callback`; for example, `item.loadAssetID = function assetID(url, callback) {}`. The callback function must be called with the asset identifier that was retrieved, or with `null` as the first parameter. The second parameter is `error`. For more information, see the [`FairPlay Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming/fps/) page.

## See Also

- [loadCertificate](mediaitem/1627435-loadcertificate.md)
  A callback function used to load the security certificate for an item.
- [loadKey](mediaitem/1627379-loadkey.md)
  A callback function used to load the security key for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/mediaitem/1627392-loadassetid)*