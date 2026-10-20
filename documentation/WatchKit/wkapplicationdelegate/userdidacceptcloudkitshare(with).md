# userDidAcceptCloudKitShare(with:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app has access to shared information in CloudKit.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
optional func userDidAcceptCloudKitShare(with cloudKitShareMetadata: CKShareMetadata)
```

```objc
- (void) userDidAcceptCloudKitShareWithMetadata:(CKShareMetadata *) cloudKitShareMetadata;
```

#### Discussion

Use this method to respond to a CloudKit Sharing invitation. In your implementation, accept the share by scheduling a [`CKAcceptSharesOperation`](../../CloudKit/ckacceptsharesoperation.md) object that contains the provided metadata object. After the user accepts the share, you can begin fetching records and incorporating the resulting data into your app.

The system launches the app, as necessary, before calling this method.

## Parameters

- `cloudKitShareMetadata`: Information about the CloudKit data that is available to the app. Use this object to retrieve information about the [`CKShare`](../../CloudKit/ckshare.md) object and the associated records that are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/userdidacceptcloudkitshare(with:))*